"""
Example: All Available Color Schemes
Generate a post for each color scheme to see the options
"""

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes

# Get all color schemes
schemes = ColorSchemes.get_all_schemes()

print(f"Generating {len(schemes)} posts, one for each color scheme...\n")

for name, scheme in schemes.items():
    generator = PostGenerator()
    
    # Create canvas
    generator.create_canvas("square", scheme.get_background_rgb())
    
    # Apply gradient
    generator.apply_gradient(
        scheme.get_primary_rgb(),
        scheme.get_secondary_rgb(),
        direction="vertical"
    )
    
    # Add vignette
    generator.add_vignette(intensity=0.4)
    
    # Add text showing the scheme name
    generator.add_text(
        scheme.name.replace('_', ' ').title(),
        position=(40, 450),
        font_size=60,
        color=scheme.get_text_rgb(),
        max_width=900,
        shadow=True
    )
    
    # Add color info
    info_text = f"Primary: {scheme.primary}\nSecondary: {scheme.secondary}\nAccent: {scheme.accent}"
    generator.add_text(
        info_text,
        position=(40, 650),
        font_size=30,
        color=scheme.get_accent_rgb(),
        max_width=900
    )
    
    # Save
    output_path = f"output/colorscheme_{name}.png"
    generator.save(output_path)
    print(f"✓ Generated: {output_path}")

print(f"\n✓ All {len(schemes)} color scheme examples completed!")
