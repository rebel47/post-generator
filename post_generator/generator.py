"""
Main Post Generator Module
Creates branded social media posts with various styles and effects
"""

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from typing import Tuple, Optional, List, Dict, Union
import os
import math
from .color_schemes import ColorScheme, ColorSchemes
from .typography import Typography


class PostGenerator:
    """Main class for generating branded social media posts"""
    
    # Standard dimensions
    DIMENSIONS = {
        "square": (1080, 1080),
        "square_large": (1200, 1200),
        "vertical": (1080, 1350),
        "story": (1080, 1920),
        "horizontal": (1200, 630),
        "linkedin_banner": (1584, 396),
        "twitter_post": (1200, 675),
    }
    
    def __init__(self, base_path: str = "."):
        """
        Initialize the post generator
        
        Args:
            base_path: Base directory path for fonts and assets
        """
        self.base_path = base_path
        self.typography = Typography(base_path)
        self.img = None
        self.draw = None
        self.width = 0
        self.height = 0
    
    def create_canvas(self, dimension: Union[str, Tuple[int, int]] = "square", 
                     color: Tuple[int, int, int] = (0, 0, 0)) -> 'PostGenerator':
        """
        Create a new canvas
        
        Args:
            dimension: Either a preset name or (width, height) tuple
            color: Background color as RGB tuple
        """
        if isinstance(dimension, str):
            if dimension not in self.DIMENSIONS:
                raise ValueError(f"Unknown dimension preset: {dimension}. Available: {list(self.DIMENSIONS.keys())}")
            self.width, self.height = self.DIMENSIONS[dimension]
        else:
            self.width, self.height = dimension
        
        self.img = Image.new("RGB", (self.width, self.height), color=color)
        self.draw = ImageDraw.Draw(self.img)
        return self
    
    def apply_gradient(self, start_color: Tuple[int, int, int], 
                      end_color: Tuple[int, int, int],
                      direction: str = "vertical") -> 'PostGenerator':
        """
        Apply a gradient to the canvas
        
        Args:
            start_color: Starting RGB color
            end_color: Ending RGB color
            direction: "vertical", "horizontal", "diagonal", "radial"
        """
        if self.img is None:
            raise ValueError("Canvas not created. Call create_canvas() first.")
        
        gradient = Image.new('RGB', (self.width, self.height))
        draw = ImageDraw.Draw(gradient)
        
        if direction == "vertical":
            for y in range(self.height):
                ratio = y / self.height
                r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
                g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
                b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
                draw.line([(0, y), (self.width, y)], fill=(r, g, b))
        
        elif direction == "horizontal":
            for x in range(self.width):
                ratio = x / self.width
                r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
                g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
                b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
                draw.line([(x, 0), (x, self.height)], fill=(r, g, b))
        
        elif direction == "diagonal":
            for y in range(self.height):
                for x in range(self.width):
                    ratio = (x + y) / (self.width + self.height)
                    r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
                    g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
                    b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
                    draw.point((x, y), fill=(r, g, b))
        
        elif direction == "radial":
            center_x, center_y = self.width // 2, self.height // 2
            max_radius = math.sqrt(center_x**2 + center_y**2)
            
            for y in range(self.height):
                for x in range(self.width):
                    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                    ratio = min(distance / max_radius, 1.0)
                    r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
                    g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
                    b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
                    draw.point((x, y), fill=(r, g, b))
        
        self.img = gradient
        self.draw = ImageDraw.Draw(self.img)
        return self
    
    def add_pattern_lines(self, color: Tuple[int, int, int] = (255, 255, 255),
                         spacing: int = 50, angle: int = 45, 
                         width: int = 2, opacity: int = 30) -> 'PostGenerator':
        """
        Add diagonal line patterns
        
        Args:
            color: Line color RGB
            spacing: Space between lines
            angle: Angle of lines (0-360)
            width: Line width
            opacity: Opacity (0-255)
        """
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        line_color = (*color, opacity)
        
        # Calculate line coordinates based on angle
        if angle == 45:
            for i in range(-self.height, self.width + self.height, spacing):
                draw.line([(i, 0), (i + self.height, self.height)], 
                         fill=line_color, width=width)
        elif angle == 135:
            for i in range(0, self.width + self.height, spacing):
                draw.line([(i, 0), (i - self.height, self.height)], 
                         fill=line_color, width=width)
        elif angle == 90:
            for i in range(0, self.width, spacing):
                draw.line([(i, 0), (i, self.height)], 
                         fill=line_color, width=width)
        elif angle == 0:
            for i in range(0, self.height, spacing):
                draw.line([(0, i), (self.width, i)], 
                         fill=line_color, width=width)
        
        # Composite overlay onto main image
        self.img = Image.alpha_composite(self.img.convert('RGBA'), overlay).convert('RGB')
        self.draw = ImageDraw.Draw(self.img)
        return self
    
    def add_geometric_shapes(self, shape_type: str = "circles",
                           color: Tuple[int, int, int] = (255, 255, 255),
                           opacity: int = 20, count: int = 10) -> 'PostGenerator':
        """
        Add geometric shape patterns
        
        Args:
            shape_type: "circles", "rectangles", "triangles"
            color: Shape color RGB
            opacity: Opacity (0-255)
            count: Number of shapes
        """
        import random
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        shape_color = (*color, opacity)
        
        for _ in range(count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(50, 200)
            
            if shape_type == "circles":
                draw.ellipse([x, y, x + size, y + size], fill=shape_color)
            elif shape_type == "rectangles":
                draw.rectangle([x, y, x + size, y + size], fill=shape_color)
            elif shape_type == "triangles":
                points = [(x, y), (x + size, y), (x + size//2, y - size)]
                draw.polygon(points, fill=shape_color)
        
        self.img = Image.alpha_composite(self.img.convert('RGBA'), overlay).convert('RGB')
        self.draw = ImageDraw.Draw(self.img)
        return self
    
    def add_vignette(self, intensity: float = 0.6) -> 'PostGenerator':
        """
        Add vignette effect (darkened edges)
        
        Args:
            intensity: Vignette intensity (0.0 to 1.0)
        """
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        center_x, center_y = self.width // 2, self.height // 2
        max_radius = math.sqrt(center_x**2 + center_y**2)
        
        for y in range(self.height):
            for x in range(self.width):
                distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
                ratio = min(distance / max_radius, 1.0)
                alpha = int(255 * ratio * intensity)
                draw.point((x, y), fill=(0, 0, 0, alpha))
        
        self.img = Image.alpha_composite(self.img.convert('RGBA'), overlay).convert('RGB')
        self.draw = ImageDraw.Draw(self.img)
        return self
    
    def add_noise(self, intensity: int = 10) -> 'PostGenerator':
        """
        Add noise texture
        
        Args:
            intensity: Noise intensity (0-50)
        """
        import random
        pixels = self.img.load()
        
        for y in range(self.height):
            for x in range(self.width):
                r, g, b = pixels[x, y]
                noise = random.randint(-intensity, intensity)
                r = max(0, min(255, r + noise))
                g = max(0, min(255, g + noise))
                b = max(0, min(255, b + noise))
                pixels[x, y] = (r, g, b)
        
        return self
    
    def add_blur(self, radius: int = 5, region: Optional[Tuple[int, int, int, int]] = None) -> 'PostGenerator':
        """
        Apply blur effect
        
        Args:
            radius: Blur radius
            region: Optional (x1, y1, x2, y2) to blur only a region
        """
        if region:
            x1, y1, x2, y2 = region
            cropped = self.img.crop((x1, y1, x2, y2))
            blurred = cropped.filter(ImageFilter.GaussianBlur(radius))
            self.img.paste(blurred, (x1, y1))
        else:
            self.img = self.img.filter(ImageFilter.GaussianBlur(radius))
        
        self.draw = ImageDraw.Draw(self.img)
        return self
    
    def add_logo(self, logo_path: str, position: str = "top-left",
                size: Tuple[int, int] = (200, 200),
                margin: int = 40, custom_position: Optional[Tuple[int, int]] = None) -> 'PostGenerator':
        """
        Add a logo to the canvas
        
        Args:
            logo_path: Path to logo file
            position: "top-left", "top-center", "top-right", "bottom-left", "bottom-center", "bottom-right", "center"
            size: Maximum logo size (will maintain aspect ratio)
            margin: Margin from edges
            custom_position: Custom (x, y) position (overrides position preset)
        """
        if not os.path.exists(logo_path):
            print(f"Warning: Logo file not found: {logo_path}")
            return self
        
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail(size, Image.Resampling.LANCZOS)
            
            # Calculate position
            if custom_position:
                x, y = custom_position
            else:
                logo_w, logo_h = logo.size
                
                if position == "top-left":
                    x, y = margin, margin
                elif position == "top-center":
                    x, y = (self.width - logo_w) // 2, margin
                elif position == "top-right":
                    x, y = self.width - logo_w - margin, margin
                elif position == "bottom-left":
                    x, y = margin, self.height - logo_h - margin
                elif position == "bottom-center":
                    x, y = (self.width - logo_w) // 2, self.height - logo_h - margin
                elif position == "bottom-right":
                    x, y = self.width - logo_w - margin, self.height - logo_h - margin
                elif position == "center":
                    x, y = (self.width - logo_w) // 2, (self.height - logo_h) // 2
                else:
                    x, y = margin, margin
            
            # Paste logo with transparency
            self.img.paste(logo, (x, y), logo)
            self.draw = ImageDraw.Draw(self.img)
        
        except Exception as e:
            print(f"Warning: Could not add logo. Error: {e}")
        
        return self
    
    def add_text(self, text: str, position: Tuple[int, int],
                font_path: str = "fonts/Poppins-Bold.ttf", font_size: int = 70,
                color: Tuple[int, int, int] = (255, 255, 255),
                max_width: Optional[int] = None, align: str = "left",
                shadow: bool = False, outline: bool = False) -> 'PostGenerator':
        """
        Add text to the canvas
        
        Args:
            text: Text content
            position: (x, y) position
            font_path: Path to font file
            font_size: Font size
            color: Text color RGB
            max_width: Maximum width for text wrapping
            align: Text alignment ("left", "center", "right")
            shadow: Add shadow effect
            outline: Add outline effect
        """
        font = self.typography.get_font(font_path, font_size)
        
        if max_width:
            self.typography.draw_multiline_text(
                self.draw, position, text, font, color, max_width, align=align
            )
        else:
            if shadow:
                self.typography.draw_text_with_shadow(
                    self.draw, position, text, font, color
                )
            elif outline:
                self.typography.draw_text_with_outline(
                    self.draw, position, text, font, color
                )
            else:
                self.draw.text(position, text, font=font, fill=color)
        
        return self
    
    def add_text_box(self, text: str, box_position: Tuple[int, int],
                    box_size: Tuple[int, int], 
                    bg_color: Tuple[int, int, int, int] = (0, 0, 0, 180),
                    text_color: Tuple[int, int, int] = (255, 255, 255),
                    font_path: str = "fonts/Poppins-Regular.ttf",
                    font_size: int = 40, padding: int = 20) -> 'PostGenerator':
        """
        Add text inside a colored box
        
        Args:
            text: Text content
            box_position: (x, y) position of box
            box_size: (width, height) of box
            bg_color: Box background color RGBA
            text_color: Text color RGB
            font_path: Font file path
            font_size: Font size
            padding: Padding inside box
        """
        x, y = box_position
        w, h = box_size
        
        # Draw semi-transparent box
        overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        draw.rectangle([x, y, x + w, y + h], fill=bg_color)
        self.img = Image.alpha_composite(self.img.convert('RGBA'), overlay).convert('RGB')
        self.draw = ImageDraw.Draw(self.img)
        
        # Add text inside box
        font = self.typography.get_font(font_path, font_size)
        text_x = x + padding
        text_y = y + padding
        max_width = w - (2 * padding)
        
        self.typography.draw_multiline_text(
            self.draw, (text_x, text_y), text, font, text_color, max_width
        )
        
        return self
    
    def save(self, output_path: str, quality: int = 95, optimize: bool = True) -> str:
        """
        Save the generated image
        
        Args:
            output_path: Output file path
            quality: JPEG quality (1-100)
            optimize: Optimize file size
        
        Returns:
            Path to saved file
        """
        if self.img is None:
            raise ValueError("No image to save. Generate content first.")
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
        
        # Save based on file extension
        if output_path.lower().endswith('.png'):
            self.img.save(output_path, "PNG", optimize=optimize)
        elif output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
            # Convert to RGB if needed (for JPEG)
            rgb_img = self.img.convert('RGB')
            rgb_img.save(output_path, "JPEG", quality=quality, optimize=optimize)
        else:
            self.img.save(output_path, optimize=optimize)
        
        print(f"✓ Generated: {output_path}")
        return output_path
    
    def show(self):
        """Display the image"""
        if self.img:
            self.img.show()
    
    def get_image(self) -> Image.Image:
        """Get the PIL Image object"""
        return self.img
