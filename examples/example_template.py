"""
Example: Using Templates
Generate posts using predefined templates
"""

import sys
import os
# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes
from post_generator.template_loader import TemplateLoader

def get_output_path(filename):
    """Get the correct output path relative to project root"""
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_dir = os.path.join(parent_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)

# First, create default templates
print("Creating default templates...")
loader = TemplateLoader()
loader.create_default_templates()

# Load a template
template = loader.load_template("professional_gradient")
color_scheme = ColorSchemes.get_scheme(template.color_scheme)

# Create generator
generator = PostGenerator()

# Create canvas
generator.create_canvas(template.dimension, color_scheme.get_background_rgb())

# Apply gradient
generator.apply_gradient(
    color_scheme.get_primary_rgb(),
    color_scheme.get_secondary_rgb(),
    template.gradient_direction
)

# Add effects
if template.add_vignette:
    generator.add_vignette(template.vignette_intensity)

# Add logo (if you have one)
# generator.add_logo("path/to/logo.png", position=template.logo_position)

# Add text
generator.add_text(
    "Unlock Your Potential",
    position=tuple(template.headline_position),
    font_size=template.headline_size,
    color=color_scheme.get_text_rgb(),
    max_width=template.headline_max_width,
    shadow=template.headline_shadow
)

# Save
generator.save(get_output_path("example_template.png"))

print("✓ Template example completed!")
print(f"\nAvailable templates: {loader.list_templates()}")
