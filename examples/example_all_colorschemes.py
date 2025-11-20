"""
Example: All Available Color Schemes
Generate a post for each color scheme to see the options
"""

import sys
import os
# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes

def get_output_path(filename):
    """Get the correct output path relative to project root"""
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_dir = os.path.join(parent_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)

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
    filename = f"colorscheme_{name}.png"
    generator.save(get_output_path(filename))
    print(f"✓ Generated: {filename}")

print(f"\n✓ All {len(schemes)} color scheme examples completed!")
