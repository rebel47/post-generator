"""
FastAPI Web API for Post Generator
Provides REST API endpoints for remote post generation
"""

from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
import uuid
import tempfile
from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes
from post_generator.template_loader import TemplateLoader
from news_fetcher import NewsFetcher


app = FastAPI(
    title="Post Generator API",
    description="Generate branded social media posts via REST API",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PostRequest(BaseModel):
    """Request model for post generation"""
    text: str
    subtext: Optional[str] = None
    template: Optional[str] = None
    dimension: str = "square"
    custom_width: Optional[int] = None
    custom_height: Optional[int] = None
    color_scheme: Optional[str] = None
    bg_color: Optional[str] = None
    gradient_start: Optional[str] = None
    gradient_end: Optional[str] = None
    gradient_direction: str = "vertical"
    pattern: Optional[str] = None
    pattern_color: Optional[str] = None
    pattern_angle: int = 45
    pattern_spacing: int = 50
    pattern_width: int = 2
    pattern_opacity: int = 30
    shape_type: Optional[str] = None
    shape_color: Optional[str] = None
    shape_count: int = 15
    shape_opacity: int = 20
    add_vignette: bool = False
    vignette_intensity: float = 0.5
    add_noise: bool = False
    noise_intensity: int = 5
    add_blur: bool = False
    blur_radius: int = 5
    text_shadow: bool = False
    text_outline: bool = False
    text_x: int = 40
    text_y: int = 400
    font_size: int = 70
    text_color: str = "#FFFFFF"
    text_max_width: int = 900
    subtext_x: int = 40
    subtext_y: int = 650
    subtext_font_size: int = 40
    subtext_color: Optional[str] = None
    logo_position: str = "top-left"
    logo_size: int = 150
    add_textbox: bool = False
    textbox_content: Optional[str] = None
    textbox_x: int = 40
    textbox_y: int = 800
    textbox_width: int = 900
    textbox_height: int = 200
    textbox_bg_color: str = "#000000"
    textbox_bg_opacity: int = 200
    textbox_text_color: str = "#FFFFFF"
    textbox_font_size: int = 35
    textbox_padding: int = 25


class TemplateInfo(BaseModel):
    """Template information model"""
    name: str
    dimension: str
    background_type: str
    color_scheme: str


@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "Post Generator API",
        "version": "1.0.0",
        "endpoints": {
            "generate": "POST /generate - Generate with file upload support (form-data)",
            "generate_json": "POST /generate/json - Generate with JSON only (for n8n/webhooks)",
            "generate_advanced": "POST /generate/advanced - Generate with all options",
            "generate_batch": "POST /generate/batch - Generate multiple posts",
            "templates": "GET /templates - List all templates",
            "template_detail": "GET /templates/{name} - Get template details",
            "color_schemes": "GET /color-schemes - List color schemes",
            "color_scheme_detail": "GET /color-schemes/{name} - Get color scheme details",
            "dimensions": "GET /dimensions - List available dimensions",
            "health": "GET /health - Health check"
        },
        "docs": "/docs - Interactive API documentation"
    }


@app.get("/dimensions")
async def list_dimensions():
    """List all available post dimensions"""
    return {
        "square": {"width": 1080, "height": 1080, "description": "Instagram post"},
        "story": {"width": 1080, "height": 1920, "description": "Instagram/Facebook story"},
        "vertical": {"width": 1080, "height": 1350, "description": "Instagram portrait"},
        "horizontal": {"width": 1200, "height": 630, "description": "Facebook/LinkedIn"},
        "wide": {"width": 1920, "height": 1080, "description": "YouTube thumbnail"},
        "banner": {"width": 1500, "height": 500, "description": "Twitter header"},
        "custom": {"width": "user-defined", "height": "user-defined", "description": "Custom size"}
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/templates", response_model=List[str])
async def list_templates():
    """List all available templates"""
    try:
        loader = TemplateLoader()
        templates = loader.list_templates()
        return templates
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/templates/{template_name}")
async def get_template(template_name: str):
    """Get template details"""
    try:
        loader = TemplateLoader()
        template = loader.load_template(template_name)
        return template.to_dict()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Template '{template_name}' not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/color-schemes", response_model=List[str])
async def list_color_schemes():
    """List all available color schemes"""
    try:
        schemes = ColorSchemes.list_schemes()
        return schemes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/color-schemes/{scheme_name}")
async def get_color_scheme(scheme_name: str):
    """Get color scheme details"""
    try:
        scheme = ColorSchemes.get_scheme(scheme_name)
        return {
            "name": scheme.name,
            "primary": scheme.primary,
            "secondary": scheme.secondary,
            "accent": scheme.accent,
            "text": scheme.text,
            "background": scheme.background
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/form")
async def generate_post_form(
    text: str = Form(...),
    subtext: Optional[str] = Form(None),
    dimension: str = Form("square"),
    custom_width: Optional[int] = Form(None),
    custom_height: Optional[int] = Form(None),
    color_scheme: Optional[str] = Form(None),
    bg_color: Optional[str] = Form(None),
    gradient_start: Optional[str] = Form(None),
    gradient_end: Optional[str] = Form(None),
    gradient_direction: str = Form("vertical"),
    pattern: Optional[str] = Form(None),
    pattern_color: Optional[str] = Form(None),
    pattern_angle: int = Form(45),
    pattern_spacing: int = Form(50),
    pattern_width: int = Form(2),
    pattern_opacity: int = Form(30),
    shape_type: Optional[str] = Form(None),
    shape_color: Optional[str] = Form(None),
    shape_count: int = Form(15),
    shape_opacity: int = Form(20),
    add_vignette: bool = Form(False),
    vignette_intensity: float = Form(0.5),
    add_noise: bool = Form(False),
    noise_intensity: int = Form(5),
    add_blur: bool = Form(False),
    blur_radius: int = Form(5),
    text_shadow: bool = Form(False),
    text_outline: bool = Form(False),
    text_x: int = Form(40),
    text_y: int = Form(400),
    font_size: int = Form(70),
    text_color: str = Form("#FFFFFF"),
    text_max_width: int = Form(900),
    subtext_x: int = Form(40),
    subtext_y: int = Form(650),
    subtext_font_size: int = Form(40),
    subtext_color: Optional[str] = Form(None),
    logo_position: str = Form("top-left"),
    logo_size: int = Form(150),
    add_textbox: bool = Form(False),
    textbox_content: Optional[str] = Form(None),
    textbox_x: int = Form(40),
    textbox_y: int = Form(800),
    textbox_width: int = Form(900),
    textbox_height: int = Form(200),
    textbox_bg_color: str = Form("#000000"),
    textbox_bg_opacity: int = Form(200),
    textbox_text_color: str = Form("#FFFFFF"),
    textbox_font_size: int = Form(35),
    textbox_padding: int = Form(25),
    logo: Optional[UploadFile] = File(None)
):
    """
    Generate post from form-data (for n8n with file uploads)
    """
    try:
        generator = PostGenerator()
        output_dir = tempfile.gettempdir()
        output_path = os.path.join(output_dir, f"post_{uuid.uuid4()}.png")
        logo_path = None
        
        # Save uploaded logo
        if logo:
            logo_path = os.path.join(output_dir, f"logo_{uuid.uuid4()}{os.path.splitext(logo.filename)[1]}")
            with open(logo_path, "wb") as f:
                f.write(await logo.read())
        
        # Canvas
        canvas_size = dimension
        if dimension == "custom" and custom_width and custom_height:
            canvas_size = (custom_width, custom_height)
        
        # Background
        bg_rgb = (0, 0, 0)
        if color_scheme:
            scheme = ColorSchemes.get_scheme(color_scheme)
            bg_rgb = scheme.get_background_rgb()
        elif bg_color:
            bg_rgb = hex_to_rgb(bg_color)
        
        generator.create_canvas(canvas_size, bg_rgb)
        
        # Gradient
        if gradient_start and gradient_end:
            start = hex_to_rgb(gradient_start)
            end = hex_to_rgb(gradient_end)
            generator.apply_gradient(start, end, gradient_direction)
        
        # Patterns
        if pattern == 'lines':
            pattern_rgb = hex_to_rgb(pattern_color) if pattern_color else (255, 255, 255)
            generator.add_pattern_lines(
                color=pattern_rgb,
                spacing=pattern_spacing,
                angle=pattern_angle,
                width=pattern_width,
                opacity=pattern_opacity
            )
        
        # Shapes
        if shape_type:
            shape_rgb = hex_to_rgb(shape_color) if shape_color else (255, 255, 255)
            generator.add_geometric_shapes(
                shape_type,
                color=shape_rgb,
                opacity=shape_opacity,
                count=shape_count
            )
        
        # Effects
        if add_vignette:
            generator.add_vignette(vignette_intensity)
        if add_noise:
            generator.add_noise(noise_intensity)
        if add_blur:
            generator.add_blur(blur_radius)
        
        # Logo
        if logo_path:
            generator.add_logo(logo_path, position=logo_position, size=(logo_size, logo_size))
        
        # Main text
        text_rgb = hex_to_rgb(text_color)
        generator.add_text(
            text,
            position=(text_x, text_y),
            font_size=font_size,
            color=text_rgb,
            max_width=text_max_width,
            shadow=text_shadow,
            outline=text_outline
        )
        
        # Subtext
        if subtext:
            subtext_rgb = hex_to_rgb(subtext_color) if subtext_color else text_rgb
            generator.add_text(
                subtext,
                position=(subtext_x, subtext_y),
                font_size=subtext_font_size,
                color=subtext_rgb,
                max_width=text_max_width
            )
        
        # Text box
        if add_textbox and textbox_content:
            tb_bg = hex_to_rgb(textbox_bg_color) + (textbox_bg_opacity,)
            tb_text = hex_to_rgb(textbox_text_color)
            generator.add_text_box(
                textbox_content,
                box_position=(textbox_x, textbox_y),
                box_size=(textbox_width, textbox_height),
                bg_color=tb_bg,
                text_color=tb_text,
                font_size=textbox_font_size,
                padding=textbox_padding
            )
        
        # Save
        generator.save(output_path)
        
        # Cleanup
        if logo_path and os.path.exists(logo_path):
            os.remove(logo_path)
        
        return FileResponse(
            output_path,
            media_type="image/png",
            filename="post.png",
            background=None
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate")
async def generate_post(
    request: PostRequest,
    logo: Optional[UploadFile] = File(None)
):
    """
    Generate a post image
    
    Returns the generated image file
    """
    try:
        generator = PostGenerator()
        output_dir = tempfile.gettempdir()
        output_path = os.path.join(output_dir, f"post_{uuid.uuid4()}.png")
        logo_path = None
        
        # Save uploaded logo if provided
        if logo:
            logo_path = os.path.join(output_dir, f"logo_{uuid.uuid4()}{os.path.splitext(logo.filename)[1]}")
            with open(logo_path, "wb") as f:
                f.write(await logo.read())
        
        # Generate using template
        if request.template:
            loader = TemplateLoader()
            template = loader.load_template(request.template)
            color_scheme = ColorSchemes.get_scheme(template.color_scheme)
            
            generator.create_canvas(template.dimension, color_scheme.get_background_rgb())
            
            if template.background_type == "gradient":
                generator.apply_gradient(
                    color_scheme.get_primary_rgb(),
                    color_scheme.get_secondary_rgb(),
                    template.gradient_direction
                )
            
            if template.pattern_type:
                if template.pattern_type == "lines":
                    generator.add_pattern_lines(
                        color_scheme.get_accent_rgb(),
                        spacing=template.pattern_spacing,
                        angle=template.pattern_angle
                    )
                else:
                    generator.add_geometric_shapes(
                        template.pattern_type,
                        color_scheme.get_accent_rgb()
                    )
            
            if template.add_vignette:
                generator.add_vignette(template.vignette_intensity)
            if template.add_noise:
                generator.add_noise(template.noise_intensity)
            
            if logo_path:
                generator.add_logo(logo_path, position=template.logo_position, 
                                 size=template.logo_size, margin=template.logo_margin)
            
            generator.add_text(
                request.text,
                position=tuple(template.headline_position),
                font_size=template.headline_size,
                color=color_scheme.get_text_rgb(),
                max_width=template.headline_max_width,
                shadow=template.headline_shadow,
                outline=template.headline_outline
            )
            
            if request.subtext and template.has_subheadline:
                generator.add_text(
                    request.subtext,
                    position=tuple(template.subheadline_position),
                    font_path=template.subheadline_font,
                    font_size=template.subheadline_size,
                    color=color_scheme.get_text_rgb(),
                    max_width=template.subheadline_max_width
                )
        
        else:
            # Custom generation
            bg_color = (0, 0, 0)
            if request.color_scheme:
                scheme = ColorSchemes.get_scheme(request.color_scheme)
                bg_color = scheme.get_background_rgb()
            elif request.bg_color:
                bg_color = hex_to_rgb(request.bg_color)
            
            # Handle custom dimensions
            canvas_size = request.dimension
            if request.dimension == "custom" and request.custom_width and request.custom_height:
                canvas_size = (request.custom_width, request.custom_height)
            
            generator.create_canvas(canvas_size, bg_color)
            
            # Gradient
            if request.gradient_start and request.gradient_end:
                start = hex_to_rgb(request.gradient_start)
                end = hex_to_rgb(request.gradient_end)
                generator.apply_gradient(start, end, request.gradient_direction)
            
            # Patterns
            if request.pattern == 'lines':
                pattern_color = hex_to_rgb(request.pattern_color) if request.pattern_color else (255, 255, 255)
                generator.add_pattern_lines(
                    color=pattern_color,
                    spacing=request.pattern_spacing,
                    angle=request.pattern_angle,
                    width=request.pattern_width,
                    opacity=request.pattern_opacity
                )
            
            # Geometric shapes
            if request.shape_type:
                shape_color = hex_to_rgb(request.shape_color) if request.shape_color else (255, 255, 255)
                generator.add_geometric_shapes(
                    request.shape_type,
                    color=shape_color,
                    opacity=request.shape_opacity,
                    count=request.shape_count
                )
            
            # Effects
            # Effects
            if request.add_vignette:
                generator.add_vignette(request.vignette_intensity)
            if request.add_noise:
                generator.add_noise(request.noise_intensity)
            if request.add_blur:
                generator.add_blur(request.blur_radius)
            
            # Logo
            if logo_path:
                generator.add_logo(logo_path, position=request.logo_position, size=(request.logo_size, request.logo_size))
            
            # Main text
            text_color = hex_to_rgb(request.text_color)
            generator.add_text(
                request.text,
                position=(request.text_x, request.text_y),
                font_size=request.font_size,
                color=text_color,
                max_width=request.text_max_width,
                shadow=request.text_shadow,
                outline=request.text_outline
            )
            
            # Subtext
            if request.subtext:
                subtext_color = hex_to_rgb(request.subtext_color) if request.subtext_color else text_color
                generator.add_text(
                    request.subtext,
                    position=(request.subtext_x, request.subtext_y),
                    font_size=request.subtext_font_size,
                    color=subtext_color,
                    max_width=request.text_max_width
                )
            
            # Text box
            if request.add_textbox and request.textbox_content:
                tb_bg = hex_to_rgb(request.textbox_bg_color) + (request.textbox_bg_opacity,)
                tb_text = hex_to_rgb(request.textbox_text_color)
                generator.add_text_box(
                    request.textbox_content,
                    box_position=(request.textbox_x, request.textbox_y),
                    box_size=(request.textbox_width, request.textbox_height),
                    bg_color=tb_bg,
                    text_color=tb_text,
                    font_size=request.textbox_font_size,
                    padding=request.textbox_padding
                )
        
        # Save and return
        generator.save(output_path)
        
        # Clean up logo if it was uploaded
        if logo_path and os.path.exists(logo_path):
            os.remove(logo_path)
        
        return FileResponse(
            output_path,
            media_type="image/png",
            filename="post.png",
            background=None
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/json")
async def generate_post_json(request: PostRequest):
    """
    Generate a post image from JSON (no file upload support)
    Perfect for n8n and webhook integrations
    
    Returns the generated image file
    """
    try:
        generator = PostGenerator()
        output_dir = tempfile.gettempdir()
        output_path = os.path.join(output_dir, f"post_{uuid.uuid4()}.png")
        
        # Determine canvas size
        canvas_size = request.dimension
        if request.dimension == "custom" and request.custom_width and request.custom_height:
            canvas_size = (request.custom_width, request.custom_height)
        
        # Background color
        bg_color = (0, 0, 0)
        if request.color_scheme:
            scheme = ColorSchemes.get_scheme(request.color_scheme)
            bg_color = scheme.get_background_rgb()
        elif request.bg_color:
            bg_color = hex_to_rgb(request.bg_color)
        
        generator.create_canvas(canvas_size, bg_color)
        
        # Gradient
        if request.gradient_start and request.gradient_end:
            start = hex_to_rgb(request.gradient_start)
            end = hex_to_rgb(request.gradient_end)
            generator.apply_gradient(start, end, request.gradient_direction)
        
        # Patterns
        if request.pattern == 'lines':
            pattern_color = hex_to_rgb(request.pattern_color) if request.pattern_color else (255, 255, 255)
            generator.add_pattern_lines(
                color=pattern_color,
                spacing=request.pattern_spacing,
                angle=request.pattern_angle,
                width=request.pattern_width,
                opacity=request.pattern_opacity
            )
        
        # Geometric shapes
        if request.shape_type:
            shape_color = hex_to_rgb(request.shape_color) if request.shape_color else (255, 255, 255)
            generator.add_geometric_shapes(
                request.shape_type,
                color=shape_color,
                opacity=request.shape_opacity,
                count=request.shape_count
            )
        
        # Effects
        if request.add_vignette:
            generator.add_vignette(request.vignette_intensity)
        if request.add_noise:
            generator.add_noise(request.noise_intensity)
        if request.add_blur:
            generator.add_blur(request.blur_radius)
        
        # Main text
        text_color = hex_to_rgb(request.text_color)
        generator.add_text(
            request.text,
            position=(request.text_x, request.text_y),
            font_size=request.font_size,
            color=text_color,
            max_width=request.text_max_width,
            shadow=request.text_shadow,
            outline=request.text_outline
        )
        
        # Subtext
        if request.subtext:
            subtext_color = hex_to_rgb(request.subtext_color) if request.subtext_color else text_color
            generator.add_text(
                request.subtext,
                position=(request.subtext_x, request.subtext_y),
                font_size=request.subtext_font_size,
                color=subtext_color,
                max_width=request.text_max_width
            )
        
        # Text box
        if request.add_textbox and request.textbox_content:
            tb_bg = hex_to_rgb(request.textbox_bg_color) + (request.textbox_bg_opacity,)
            tb_text = hex_to_rgb(request.textbox_text_color)
            generator.add_text_box(
                request.textbox_content,
                box_position=(request.textbox_x, request.textbox_y),
                box_size=(request.textbox_width, request.textbox_height),
                bg_color=tb_bg,
                text_color=tb_text,
                font_size=request.textbox_font_size,
                padding=request.textbox_padding
            )
        
        # Save
        generator.save(output_path)
        
        return FileResponse(
            output_path,
            media_type="image/png",
            filename="post.png",
            background=None
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/batch")
async def generate_batch(posts: List[PostRequest]):
    """
    Generate multiple posts in batch
    
    Returns a list of generated image URLs
    """
    try:
        results = []
        
        for i, request in enumerate(posts):
            generator = PostGenerator()
            output_dir = tempfile.gettempdir()
            output_path = os.path.join(output_dir, f"post_batch_{i}_{uuid.uuid4()}.png")
            
            # Simple generation for batch (without logo upload support)
            bg_color = (0, 0, 0)
            if request.color_scheme:
                scheme = ColorSchemes.get_scheme(request.color_scheme)
                bg_color = scheme.get_background_rgb()
            
            generator.create_canvas(request.dimension, bg_color)
            
            if request.gradient_start and request.gradient_end:
                start = hex_to_rgb(request.gradient_start)
                end = hex_to_rgb(request.gradient_end)
                generator.apply_gradient(start, end, request.gradient_direction)
            
            text_color = hex_to_rgb(request.text_color)
            generator.add_text(
                request.text,
                position=(40, 400),
                font_size=request.font_size,
                color=text_color,
                max_width=900
            )
            
            generator.save(output_path)
            results.append({"index": i, "path": output_path})
        
        return JSONResponse(content={"generated": len(results), "files": results})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BatchTextRequest(BaseModel):
    """Request for batch generation with same design, different text"""
    texts: List[str]  # List of different text content
    design: PostRequest  # Common design settings
    logo_url: Optional[str] = None  # Optional logo URL to download


@app.post("/generate/batch-smart")
async def generate_batch_smart(batch: BatchTextRequest):
    """
    Generate multiple posts with same design but different text
    Perfect for n8n: same logo, gradient, effects - just different text
    
    Returns ZIP file with all images
    """
    try:
        import zipfile
        import io
        from fastapi.responses import StreamingResponse
        
        output_dir = tempfile.gettempdir()
        results = []
        logo_path = None
        
        # Download logo once if provided
        if batch.logo_url:
            import requests
            logo_ext = batch.logo_url.split('.')[-1]
            logo_path = os.path.join(output_dir, f"batch_logo_{uuid.uuid4()}.{logo_ext}")
            response = requests.get(batch.logo_url)
            with open(logo_path, 'wb') as f:
                f.write(response.content)
        
        # Generate each post
        for i, text in enumerate(batch.texts):
            generator = PostGenerator()
            output_path = os.path.join(output_dir, f"post_{i+1}.png")
            
            # Canvas
            canvas_size = batch.design.dimension
            if batch.design.dimension == "custom" and batch.design.custom_width and batch.design.custom_height:
                canvas_size = (batch.design.custom_width, batch.design.custom_height)
            
            # Background
            bg_color = (0, 0, 0)
            if batch.design.color_scheme:
                scheme = ColorSchemes.get_scheme(batch.design.color_scheme)
                bg_color = scheme.get_background_rgb()
            elif batch.design.bg_color:
                bg_color = hex_to_rgb(batch.design.bg_color)
            
            generator.create_canvas(canvas_size, bg_color)
            
            # Gradient
            if batch.design.gradient_start and batch.design.gradient_end:
                start = hex_to_rgb(batch.design.gradient_start)
                end = hex_to_rgb(batch.design.gradient_end)
                generator.apply_gradient(start, end, batch.design.gradient_direction)
            
            # Patterns
            if batch.design.pattern == 'lines':
                pattern_color = hex_to_rgb(batch.design.pattern_color) if batch.design.pattern_color else (255, 255, 255)
                generator.add_pattern_lines(
                    color=pattern_color,
                    spacing=batch.design.pattern_spacing,
                    angle=batch.design.pattern_angle,
                    width=batch.design.pattern_width,
                    opacity=batch.design.pattern_opacity
                )
            
            # Shapes
            if batch.design.shape_type:
                shape_color = hex_to_rgb(batch.design.shape_color) if batch.design.shape_color else (255, 255, 255)
                generator.add_geometric_shapes(
                    batch.design.shape_type,
                    color=shape_color,
                    opacity=batch.design.shape_opacity,
                    count=batch.design.shape_count
                )
            
            # Effects
            if batch.design.add_vignette:
                generator.add_vignette(batch.design.vignette_intensity)
            if batch.design.add_noise:
                generator.add_noise(batch.design.noise_intensity)
            if batch.design.add_blur:
                generator.add_blur(batch.design.blur_radius)
            
            # Logo (same for all)
            if logo_path:
                generator.add_logo(logo_path, position=batch.design.logo_position, 
                                 size=(batch.design.logo_size, batch.design.logo_size))
            
            # Text (different for each)
            text_color = hex_to_rgb(batch.design.text_color)
            generator.add_text(
                text,
                position=(batch.design.text_x, batch.design.text_y),
                font_size=batch.design.font_size,
                color=text_color,
                max_width=batch.design.text_max_width,
                shadow=batch.design.text_shadow,
                outline=batch.design.text_outline
            )
            
            # Subtext (if design has it)
            if batch.design.subtext:
                subtext_color = hex_to_rgb(batch.design.subtext_color) if batch.design.subtext_color else text_color
                generator.add_text(
                    batch.design.subtext,
                    position=(batch.design.subtext_x, batch.design.subtext_y),
                    font_size=batch.design.subtext_font_size,
                    color=subtext_color,
                    max_width=batch.design.text_max_width
                )
            
            # Text box (if design has it)
            if batch.design.add_textbox and batch.design.textbox_content:
                tb_bg = hex_to_rgb(batch.design.textbox_bg_color) + (batch.design.textbox_bg_opacity,)
                tb_text = hex_to_rgb(batch.design.textbox_text_color)
                generator.add_text_box(
                    batch.design.textbox_content,
                    box_position=(batch.design.textbox_x, batch.design.textbox_y),
                    box_size=(batch.design.textbox_width, batch.design.textbox_height),
                    bg_color=tb_bg,
                    text_color=tb_text,
                    font_size=batch.design.textbox_font_size,
                    padding=batch.design.textbox_padding
                )
            
            generator.save(output_path)
            results.append(output_path)
        
        # Cleanup logo
        if logo_path and os.path.exists(logo_path):
            os.remove(logo_path)
        
        # Create ZIP file
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for i, file_path in enumerate(results):
                zip_file.write(file_path, f"post_{i+1}.png")
                os.remove(file_path)  # Clean up
        
        zip_buffer.seek(0)
        
        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={"Content-Disposition": f"attachment; filename=posts_batch_{len(batch.texts)}.zip"}
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# NEWS FETCHER ENDPOINTS
# ============================================================================

# Initialize news fetcher (lazy loading)
_news_fetcher = None

def get_news_fetcher(
    language: str = 'en',
    country: str = 'US',
    period: str = '7d',
    max_results: int = 10
):
    """Get or create news fetcher instance"""
    return NewsFetcher(
        language=language,
        country=country,
        period=period,
        max_results=max_results
    )


@app.get("/news/top")
async def get_top_news(
    language: str = 'en',
    country: str = 'US',
    period: str = '7d',
    max_results: int = 10
):
    """
    Get top news headlines
    
    Args:
        language: Language code (default: 'en')
        country: Country code (default: 'US')
        period: Time period (7d, 1m, 1y)
        max_results: Maximum number of results (default: 10)
    
    Returns:
        List of top news articles
    
    Example:
        GET /news/top?country=US&period=7d&max_results=5
    """
    try:
        fetcher = get_news_fetcher(language, country, period, max_results)
        articles = fetcher.get_top_news()
        
        return {
            "status": "success",
            "count": len(articles),
            "language": language,
            "country": country,
            "period": period,
            "articles": articles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top news: {str(e)}")


@app.get("/news/search")
async def search_news(
    keyword: str,
    language: str = 'en',
    country: str = 'US',
    period: str = '7d',
    max_results: int = 10
):
    """
    Search news by keyword
    
    Args:
        keyword: Search keyword (required)
        language: Language code
        country: Country code
        period: Time period
        max_results: Maximum results
    
    Returns:
        List of news articles matching keyword
    
    Example:
        GET /news/search?keyword=artificial+intelligence&max_results=5
    """
    try:
        fetcher = get_news_fetcher(language, country, period, max_results)
        articles = fetcher.get_news_by_keyword(keyword)
        
        return {
            "status": "success",
            "keyword": keyword,
            "count": len(articles),
            "language": language,
            "country": country,
            "period": period,
            "articles": articles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching news: {str(e)}")


@app.get("/news/topic/{topic}")
async def get_news_by_topic(
    topic: str,
    language: str = 'en',
    country: str = 'US',
    period: str = '7d',
    max_results: int = 10
):
    """
    Get news by topic
    
    Args:
        topic: Topic name (WORLD, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, etc.)
        language: Language code
        country: Country code
        period: Time period
        max_results: Maximum results
    
    Returns:
        List of news articles for the topic
    
    Example:
        GET /news/topic/TECHNOLOGY?max_results=5
    """
    try:
        fetcher = get_news_fetcher(language, country, period, max_results)
        articles = fetcher.get_news_by_topic(topic)
        
        return {
            "status": "success",
            "topic": topic.upper(),
            "count": len(articles),
            "language": language,
            "country": country,
            "period": period,
            "articles": articles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news by topic: {str(e)}")


@app.get("/news/location")
async def get_news_by_location(
    location: str,
    language: str = 'en',
    country: str = 'US',
    period: str = '7d',
    max_results: int = 10
):
    """
    Get news by location
    
    Args:
        location: City/state/country name (required)
        language: Language code
        country: Country code
        period: Time period
        max_results: Maximum results
    
    Returns:
        List of news articles for the location
    
    Example:
        GET /news/location?location=New+York&max_results=5
    """
    try:
        fetcher = get_news_fetcher(language, country, period, max_results)
        articles = fetcher.get_news_by_location(location)
        
        return {
            "status": "success",
            "location": location,
            "count": len(articles),
            "language": language,
            "country": country,
            "period": period,
            "articles": articles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news by location: {str(e)}")


@app.get("/news/site")
async def get_news_by_site(
    site: str,
    language: str = 'en',
    country: str = 'US',
    period: str = '7d',
    max_results: int = 10
):
    """
    Get news from specific website
    
    Args:
        site: Website domain (e.g., 'cnn.com', 'bbc.com')
        language: Language code
        country: Country code
        period: Time period
        max_results: Maximum results
    
    Returns:
        List of news articles from the site
    
    Example:
        GET /news/site?site=cnn.com&max_results=5
    """
    try:
        fetcher = get_news_fetcher(language, country, period, max_results)
        articles = fetcher.get_news_by_site(site)
        
        return {
            "status": "success",
            "site": site,
            "count": len(articles),
            "language": language,
            "country": country,
            "period": period,
            "articles": articles
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news by site: {str(e)}")


@app.get("/news/article")
async def get_full_article(url: str):
    """
    Get full article content
    
    Args:
        url: Article URL (required)
    
    Returns:
        Full article with title, text, images, etc.
    
    Example:
        GET /news/article?url=https://example.com/article
    """
    try:
        fetcher = NewsFetcher()
        article = fetcher.get_full_article(url)
        
        if 'error' in article:
            raise HTTPException(status_code=404, detail=article['error'])
        
        return {
            "status": "success",
            "article": article
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching article: {str(e)}")


@app.get("/news/available-countries")
async def get_available_countries():
    """
    Get list of available countries
    
    Returns:
        Dictionary of country names and codes
    
    Example:
        GET /news/available-countries
    """
    try:
        countries = NewsFetcher.get_available_countries()
        return {
            "status": "success",
            "count": len(countries),
            "countries": countries
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching countries: {str(e)}")


@app.get("/news/available-languages")
async def get_available_languages():
    """
    Get list of available languages
    
    Returns:
        Dictionary of language names and codes
    
    Example:
        GET /news/available-languages
    """
    try:
        languages = NewsFetcher.get_available_languages()
        return {
            "status": "success",
            "count": len(languages),
            "languages": languages
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching languages: {str(e)}")


@app.get("/news/topics")
async def get_available_topics():
    """
    Get list of available news topics
    
    Returns:
        List of topic names
    
    Example:
        GET /news/topics
    """
    return {
        "status": "success",
        "topics": NewsFetcher.TOPICS
    }


def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    import uvicorn
    print("Starting Post Generator API...")
    print("API will be available at: http://localhost:8000")
    print("API docs at: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
