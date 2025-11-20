"""
Example: Text Box with Background
Create posts with text inside colored boxes
"""

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes

# Get color scheme
color_scheme = ColorSchemes.CORPORATE_TECH

# Create generator
generator = PostGenerator()

# Create canvas
generator.create_canvas("square", color_scheme.get_background_rgb())

# Apply horizontal gradient
generator.apply_gradient(
    color_scheme.get_primary_rgb(),
    color_scheme.get_secondary_rgb(),
    direction="horizontal"
)

# Add logo (if available)
# generator.add_logo("logo.png", position="top-left", size=(200, 200))

# Add headline
generator.add_text(
    "Annual Report 2025",
    position=(40, 300),
    font_size=75,
    color=color_scheme.get_text_rgb(),
    shadow=True
)

# Add text box with statistics
generator.add_text_box(
    text="Revenue Growth: 45%\nCustomer Base: 10M+\nGlobal Presence: 50+ Countries",
    box_position=(40, 650),
    box_size=(1000, 280),
    bg_color=(0, 0, 0, 200),
    text_color=color_scheme.get_text_rgb(),
    font_size=40,
    padding=30
)

# Save
generator.save("output/example_textbox.png")

print("✓ Text box example completed!")
