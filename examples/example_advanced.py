"""
Example: Advanced Styling
Demonstrates advanced styling features
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

# Get a color scheme
color_scheme = ColorSchemes.BOLD_PURPLE

# Create generator
generator = PostGenerator()

# Create vertical canvas (story format)
generator.create_canvas("story", color_scheme.get_background_rgb())

# Apply radial gradient
generator.apply_gradient(
    color_scheme.get_primary_rgb(),
    color_scheme.get_secondary_rgb(),
    direction="radial"
)

# Add diagonal line pattern
generator.add_pattern_lines(
    color=color_scheme.get_accent_rgb(),
    spacing=60,
    angle=45,
    width=3,
    opacity=40
)

# Add geometric shapes
generator.add_geometric_shapes(
    shape_type="circles",
    color=(255, 255, 255),
    opacity=15,
    count=15
)

# Add vignette
generator.add_vignette(intensity=0.5)

# Add noise texture
generator.add_noise(intensity=8)

# Add text with outline
generator.add_text(
    "The Future\nis Now",
    position=(60, 700),
    font_size=100,
    color=color_scheme.get_text_rgb(),
    max_width=960,
    outline=True
)

# Add subtext
generator.add_text(
    "Join the revolution",
    position=(60, 1000),
    font_size=50,
    color=color_scheme.get_accent_rgb(),
    max_width=960
)

# Save
generator.save(get_output_path("example_advanced.png"))

print("✓ Advanced styling example completed!")
