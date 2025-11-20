"""
Example: Using Templates
Generate posts using predefined templates
"""

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes
from post_generator.template_loader import TemplateLoader

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
generator.save("output/example_template.png")

print("✓ Template example completed!")
print(f"\nAvailable templates: {loader.list_templates()}")
