"""
Example: Basic Post Generation
Simple example showing how to create a basic post
"""

from post_generator import PostGenerator

# Create a generator instance
generator = PostGenerator()

# Create a square canvas with black background
generator.create_canvas("square", color=(0, 0, 0))

# Apply a red-to-black gradient
generator.apply_gradient(
    start_color=(255, 0, 0),
    end_color=(0, 0, 0),
    direction="vertical"
)

# Add text
generator.add_text(
    text="Innovation Starts Here",
    position=(40, 400),
    font_size=70,
    color=(255, 255, 255),
    max_width=900,
    shadow=True
)

# Save the image
generator.save("output/example_basic.png")

print("✓ Basic example completed!")
