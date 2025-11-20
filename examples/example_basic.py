"""
Example: Basic Post Generation
Simple example showing how to create a basic post
"""

import sys
import os
# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from post_generator import PostGenerator

def get_output_path(filename):
    """Get the correct output path relative to project root"""
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output_dir = os.path.join(parent_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)

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
generator.save(get_output_path("example_basic.png"))

print("✓ Basic example completed!")
