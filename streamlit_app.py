"""
Streamlit UI for Post Generator
Simple visual interface to create social media posts
"""

import streamlit as st
import os
import sys
from PIL import Image

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes

# Page config
st.set_page_config(
    page_title="Post Generator",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Social Media Post Generator")
st.markdown("Create stunning social media posts with custom designs")

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("⚙️ Design Settings")
    
    # Canvas settings
    st.subheader("1. Canvas")
    dimension = st.selectbox(
        "Post Size",
        ["square", "story", "vertical", "horizontal", "wide", "banner", "custom"],
        help="Choose the dimensions for your post"
    )
    
    if dimension == "custom":
        custom_width = st.number_input("Width (px)", value=1080, min_value=100, max_value=5000)
        custom_height = st.number_input("Height (px)", value=1080, min_value=100, max_value=5000)
    
    # Background
    st.subheader("2. Background")
    bg_type = st.radio("Background Type", ["Color", "Gradient"])
    
    if bg_type == "Color":
        bg_color = st.color_picker("Background Color", "#000000")
    else:
        gradient_start = st.color_picker("Gradient Start Color", "#FF0000")
        gradient_end = st.color_picker("Gradient End Color", "#000000")
        gradient_direction = st.selectbox(
            "Gradient Direction",
            ["vertical", "horizontal", "diagonal", "diagonal_reverse", "radial"]
        )
    
    # Optional color scheme
    use_color_scheme = st.checkbox("Use Preset Color Scheme (overrides colors above)")
    if use_color_scheme:
        schemes = ColorSchemes.get_all_schemes()
        scheme_name = st.selectbox("Color Scheme", list(schemes.keys()))
    
    # Logo upload
    st.subheader("3. Logo (Optional)")
    logo_file = st.file_uploader("Upload Logo", type=["png", "jpg", "jpeg"])
    
    if logo_file:
        logo_position = st.selectbox(
            "Logo Position",
            ["top-left", "top-center", "top-right", "bottom-left", "bottom-center", "bottom-right", "center"]
        )
        logo_size = st.slider("Logo Size", 50, 500, 150, 10)
    
    # Additional Image upload
    st.subheader("4. Additional Image (Optional)")
    additional_image_file = st.file_uploader("Upload Additional Image", type=["png", "jpg", "jpeg"])
    
    if additional_image_file:
        additional_image_position = st.selectbox(
            "Image Position",
            ["center", "top-left", "top-center", "top-right", "bottom-left", "bottom-center", "bottom-right"],
            key="additional_image_position"
        )
        additional_image_size = st.slider("Image Max Size (0 = original)", 0, 1000, 400, 50, key="additional_image_size")
        additional_image_opacity = st.slider("Image Opacity", 0, 255, 255, 5, key="additional_image_opacity")
    
    # Effects
    st.subheader("5. Effects")
    
    add_vignette = st.checkbox("Add Vignette")
    if add_vignette:
        vignette_intensity = st.slider("Vignette Intensity", 0.0, 1.0, 0.5, 0.1)
    
    add_noise = st.checkbox("Add Noise Texture")
    if add_noise:
        noise_intensity = st.slider("Noise Intensity", 1, 20, 5, 1)
    
    add_blur = st.checkbox("Add Blur Effect")
    if add_blur:
        blur_radius = st.slider("Blur Radius", 1, 20, 5, 1)
    
    # Patterns
    st.subheader("6. Patterns (Optional)")
    add_pattern = st.checkbox("Add Pattern")
    
    if add_pattern:
        pattern_type = st.radio("Pattern Type", ["Lines", "Geometric Shapes"])
        
        if pattern_type == "Lines":
            pattern_color = st.color_picker("Pattern Color", "#FFFFFF")
            line_spacing = st.slider("Line Spacing", 10, 200, 50, 10)
            line_angle = st.slider("Line Angle", 0, 180, 45, 15)
            line_width = st.slider("Line Width", 1, 10, 2, 1)
            line_opacity = st.slider("Line Opacity", 0, 100, 30, 5)
        else:
            shape_type = st.selectbox("Shape Type", ["circles", "rectangles", "triangles"])
            shape_color = st.color_picker("Shape Color", "#FFFFFF")
            shape_count = st.slider("Number of Shapes", 5, 50, 15, 5)
            shape_opacity = st.slider("Shape Opacity", 0, 100, 20, 5)

with col2:
    st.header("📝 Text Content")
    
    # Main text
    st.subheader("Main Text")
    main_text = st.text_area(
        "Text Content", 
        "Your Amazing\nHeadline Here", 
        height=100,
        help="Press Enter to create new lines"
    )
    
    main_col1, main_col2 = st.columns(2)
    with main_col1:
        main_x = st.number_input("Text X Position", value=40, min_value=0, step=10)
        main_font_size = st.slider("Font Size", 20, 150, 70, 5)
    with main_col2:
        main_y = st.number_input("Text Y Position", value=400, min_value=0, step=10)
        main_max_width = st.number_input("Max Width", value=900, min_value=100, step=50)
    
    main_text_color = st.color_picker("Text Color", "#FFFFFF")
    
    main_effects_col1, main_effects_col2 = st.columns(2)
    with main_effects_col1:
        main_shadow = st.checkbox("Shadow", value=True)
    with main_effects_col2:
        main_outline = st.checkbox("Outline")
    
    st.markdown("---")
    
    # Secondary text (optional)
    add_secondary = st.checkbox("Add Secondary Text")
    if add_secondary:
        st.subheader("Secondary Text")
        secondary_text = st.text_area(
            "Secondary Text", 
            "Your tagline or subtext", 
            height=60,
            help="Press Enter for new lines"
        )
        
        sec_col1, sec_col2 = st.columns(2)
        with sec_col1:
            sec_x = st.number_input("Secondary X", value=40, min_value=0, step=10)
            sec_font_size = st.slider("Secondary Font Size", 20, 100, 40, 5)
        with sec_col2:
            sec_y = st.number_input("Secondary Y", value=650, min_value=0, step=10)
            sec_max_width = st.number_input("Secondary Max Width", value=900, min_value=100, step=50)
        
        secondary_text_color = st.color_picker("Secondary Text Color", "#AAAAAA")
        sec_shadow = st.checkbox("Secondary Shadow")
    
    st.markdown("---")
    
    # Text box (optional)
    add_textbox = st.checkbox("Add Text Box")
    if add_textbox:
        st.subheader("Text Box")
        textbox_content = st.text_area(
            "Text Box Content", 
            "• Feature 1\n• Feature 2\n• Feature 3", 
            height=80,
            help="Press Enter for new lines"
        )
        
        tb_col1, tb_col2 = st.columns(2)
        with tb_col1:
            tb_x = st.number_input("Box X", value=40, min_value=0, step=10)
            tb_width = st.number_input("Box Width", value=900, min_value=100, step=50)
            tb_font_size = st.slider("Box Font Size", 20, 80, 35, 5)
        with tb_col2:
            tb_y = st.number_input("Box Y", value=800, min_value=0, step=10)
            tb_height = st.number_input("Box Height", value=200, min_value=50, step=10)
            tb_padding = st.slider("Box Padding", 10, 60, 25, 5)
        
        tb_bg_color = st.color_picker("Box Background Color", "#000000")
        tb_bg_opacity = st.slider("Box Background Opacity", 0, 255, 200, 5)
        tb_text_color = st.color_picker("Box Text Color", "#FFFFFF")

# Generate button
st.markdown("---")
generate_col1, generate_col2, generate_col3 = st.columns([1, 1, 1])

with generate_col2:
    filename = st.text_input("Filename", "my_awesome_post.png")
    generate_button = st.button("🚀 Generate Post", type="primary", use_container_width=True)

# Generate the post
if generate_button:
    try:
        with st.spinner("Creating your amazing post..."):
            # Initialize generator
            gen = PostGenerator()
            
            # Create canvas
            if dimension == "custom":
                canvas_size = (custom_width, custom_height)
            else:
                canvas_size = dimension
            
            # Determine background color
            if use_color_scheme:
                color_scheme = ColorSchemes.get_scheme(scheme_name)
                bg_rgb = color_scheme.get_background_rgb()
            elif bg_type == "Color":
                bg_rgb = tuple(int(bg_color[i:i+2], 16) for i in (1, 3, 5))
            else:
                bg_rgb = (0, 0, 0)
            
            gen.create_canvas(canvas_size, bg_rgb)
            
            # Apply gradient
            if bg_type == "Gradient":
                if use_color_scheme:
                    start_rgb = color_scheme.get_primary_rgb()
                    end_rgb = color_scheme.get_secondary_rgb()
                else:
                    start_rgb = tuple(int(gradient_start[i:i+2], 16) for i in (1, 3, 5))
                    end_rgb = tuple(int(gradient_end[i:i+2], 16) for i in (1, 3, 5))
                
                gen.apply_gradient(start_rgb, end_rgb, gradient_direction)
            
            # Add patterns
            if add_pattern:
                if pattern_type == "Lines":
                    pattern_rgb = tuple(int(pattern_color[i:i+2], 16) for i in (1, 3, 5))
                    gen.add_pattern_lines(
                        pattern_rgb,
                        spacing=line_spacing,
                        angle=line_angle,
                        width=line_width,
                        opacity=line_opacity
                    )
                else:
                    shape_rgb = tuple(int(shape_color[i:i+2], 16) for i in (1, 3, 5))
                    gen.add_geometric_shapes(
                        shape_type,
                        shape_rgb,
                        opacity=shape_opacity,
                        count=shape_count
                    )
            
            # Add effects
            if add_vignette:
                gen.add_vignette(vignette_intensity)
            
            if add_noise:
                gen.add_noise(noise_intensity)
            
            if add_blur:
                gen.add_blur(blur_radius)
            
            # Add logo
            if logo_file:
                # Save uploaded logo temporarily
                temp_logo_path = os.path.join("output", "temp_logo.png")
                os.makedirs("output", exist_ok=True)
                with open(temp_logo_path, "wb") as f:
                    f.write(logo_file.getbuffer())
                
                gen.add_logo(
                    temp_logo_path,
                    position=logo_position,
                    size=(logo_size, logo_size)
                )
            
            # Add additional image
            if additional_image_file:
                # Save uploaded image temporarily
                temp_image_path = os.path.join("output", "temp_additional_image.png")
                os.makedirs("output", exist_ok=True)
                with open(temp_image_path, "wb") as f:
                    f.write(additional_image_file.getbuffer())
                
                img_size = (additional_image_size, additional_image_size) if additional_image_size > 0 else None
                gen.add_image(
                    temp_image_path,
                    position=additional_image_position,
                    size=img_size,
                    opacity=additional_image_opacity
                )
            
            # Add main text
            main_rgb = tuple(int(main_text_color[i:i+2], 16) for i in (1, 3, 5))
            gen.add_text(
                main_text,
                position=(main_x, main_y),
                font_size=main_font_size,
                color=main_rgb,
                max_width=main_max_width,
                shadow=main_shadow,
                outline=main_outline
            )
            
            # Add secondary text
            if add_secondary:
                sec_rgb = tuple(int(secondary_text_color[i:i+2], 16) for i in (1, 3, 5))
                gen.add_text(
                    secondary_text,
                    position=(sec_x, sec_y),
                    font_size=sec_font_size,
                    color=sec_rgb,
                    max_width=sec_max_width,
                    shadow=sec_shadow
                )
            
            # Add text box
            if add_textbox:
                tb_bg_rgb = tuple(int(tb_bg_color[i:i+2], 16) for i in (1, 3, 5))
                tb_bg_rgba = tb_bg_rgb + (tb_bg_opacity,)
                tb_text_rgb = tuple(int(tb_text_color[i:i+2], 16) for i in (1, 3, 5))
                
                gen.add_text_box(
                    textbox_content,
                    box_position=(tb_x, tb_y),
                    box_size=(tb_width, tb_height),
                    bg_color=tb_bg_rgba,
                    text_color=tb_text_rgb,
                    font_size=tb_font_size,
                    padding=tb_padding
                )
            
            # Save the image
            output_path = os.path.join("output", filename)
            gen.save(output_path)
            
            # Display the result
            st.success("✅ Post generated successfully!")
            
            # Show the image
            generated_image = Image.open(output_path)
            st.image(generated_image, caption=filename, use_container_width=True)
            
            # Download button
            with open(output_path, "rb") as file:
                st.download_button(
                    label="⬇️ Download Post",
                    data=file,
                    file_name=filename,
                    mime="image/png",
                    use_container_width=True
                )
    
    except Exception as e:
        st.error(f"❌ Error generating post: {str(e)}")
        st.exception(e)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>Built with ❤️ using Streamlit | Post Generator v1.0</p>
    </div>
    """,
    unsafe_allow_html=True
)
