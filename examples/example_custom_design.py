"""
Example: Complete Custom Design
Build posts from scratch with full control over every element
"""

import sys
import os
# Add parent directory to path to import post_generator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from post_generator import PostGenerator

# Helper function to get output path
def get_output_path(filename):
    """Get the correct output path in parent directory"""
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'output'))
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)

def example_1_fully_custom():
    """Completely custom design with precise control"""
    print("\n1. Creating fully custom design...")
    
    gen = PostGenerator()
    
    # Custom dimension
    gen.create_canvas((1200, 1200), color=(10, 10, 30))
    
    # Custom diagonal gradient with your exact colors
    gen.apply_gradient(
        start_color=(138, 43, 226),  # Purple
        end_color=(255, 20, 147),    # Deep pink
        direction="diagonal"
    )
    
    # Add multiple pattern layers
    gen.add_pattern_lines(
        color=(255, 255, 255),
        spacing=80,
        angle=30,
        width=2,
        opacity=15
    )
    
    gen.add_pattern_lines(
        color=(255, 255, 255),
        spacing=80,
        angle=150,  # Cross pattern
        width=2,
        opacity=15
    )
    
    # Add geometric shapes
    gen.add_geometric_shapes(
        shape_type="circles",
        color=(255, 255, 255),
        opacity=10,
        count=25
    )
    
    # Custom vignette
    gen.add_vignette(intensity=0.7)
    
    # Add noise for texture
    gen.add_noise(intensity=8)
    
    # Multiple text layers with precise positioning
    gen.add_text(
        "CUSTOM",
        position=(60, 300),
        font_size=120,
        color=(255, 255, 255),
        outline=True
    )
    
    gen.add_text(
        "DESIGN",
        position=(60, 450),
        font_size=120,
        color=(255, 223, 0),  # Gold
        shadow=True
    )
    
    gen.add_text(
        "Your brand, your style, your rules",
        position=(60, 650),
        font_size=40,
        color=(200, 200, 255),
        max_width=1080
    )
    
    # Add a semi-transparent text box
    gen.add_text_box(
        text="100% Customizable • No Limits • Full Control",
        box_position=(60, 950),
        box_size=(1080, 150),
        bg_color=(0, 0, 0, 200),
        text_color=(255, 255, 255),
        font_size=35,
        padding=30
    )
    
    output_path = get_output_path("custom_design_1.png")
    gen.save(output_path)
    print(f"   ✓ Saved: {output_path}")


def example_2_brand_colors():
    """Custom design with specific brand colors"""
    print("\n2. Creating design with custom brand colors...")
    
    # Your brand colors
    BRAND_PRIMARY = (0, 102, 204)      # Blue
    BRAND_SECONDARY = (255, 102, 0)    # Orange
    BRAND_ACCENT = (0, 204, 153)       # Teal
    BRAND_DARK = (20, 20, 40)
    
    gen = PostGenerator()
    gen.create_canvas("square", BRAND_DARK)
    
    # Brand gradient
    gen.apply_gradient(BRAND_PRIMARY, BRAND_DARK, "vertical")
    
    # Brand accent lines
    gen.add_pattern_lines(
        color=BRAND_ACCENT,
        spacing=60,
        angle=45,
        opacity=40
    )
    
    gen.add_vignette(0.5)
    
    # Brand text
    gen.add_text(
        "Your Brand",
        position=(40, 350),
        font_size=90,
        color=(255, 255, 255),
        shadow=True
    )
    
    gen.add_text(
        "Your Colors",
        position=(40, 480),
        font_size=90,
        color=BRAND_SECONDARY,
        outline=True
    )
    
    gen.add_text(
        "Your Identity",
        position=(40, 610),
        font_size=60,
        color=BRAND_ACCENT
    )
    
    gen.save(get_output_path("custom_brand_colors.png"))
    print("   ✓ Saved: custom_brand_colors.png")


def example_3_layered_effects():
    """Stack multiple effects for unique look"""
    print("\n3. Creating layered effects design...")
    
    gen = PostGenerator()
    gen.create_canvas("square", (0, 0, 0))
    
    # Layer 1: Base gradient
    gen.apply_gradient((40, 0, 60), (0, 0, 0), "radial")
    
    # Layer 2: First pattern
    gen.add_pattern_lines(
        color=(100, 0, 150),
        spacing=50,
        angle=0,
        width=3,
        opacity=30
    )
    
    # Layer 3: Second pattern (perpendicular)
    gen.add_pattern_lines(
        color=(150, 0, 200),
        spacing=50,
        angle=90,
        width=3,
        opacity=30
    )
    
    # Layer 4: Geometric shapes
    gen.add_geometric_shapes("rectangles", (255, 0, 255), opacity=15, count=15)
    
    # Layer 5: Vignette
    gen.add_vignette(0.6)
    
    # Layer 6: Subtle noise
    gen.add_noise(5)
    
    # Text with custom styling
    gen.add_text(
        "LAYERED\nEFFECTS",
        position=(40, 400),
        font_size=100,
        color=(255, 255, 255),
        max_width=1000,
        outline=True
    )
    
    gen.save(get_output_path("custom_layered.png"))
    print("   ✓ Saved: custom_layered.png")


def example_4_minimalist_custom():
    """Custom minimalist design"""
    print("\n4. Creating custom minimalist design...")
    
    gen = PostGenerator()
    
    # Custom light background
    gen.create_canvas("square", (250, 250, 250))
    
    # Very subtle gradient
    gen.apply_gradient((250, 250, 250), (240, 240, 245), "vertical")
    
    # Single accent line
    gen.add_pattern_lines(
        color=(200, 200, 210),
        spacing=1080,  # Just one line
        angle=90,
        width=5,
        opacity=100
    )
    
    # Minimal text - top aligned
    gen.add_text(
        "MINIMAL",
        position=(40, 40),
        font_size=60,
        color=(50, 50, 50)
    )
    
    # Main message - centered
    gen.add_text(
        "Less is More",
        position=(40, 450),
        font_size=80,
        color=(30, 30, 30)
    )
    
    # Subtle footer
    gen.add_text(
        "Custom minimalist design",
        position=(40, 1000),
        font_size=30,
        color=(150, 150, 150)
    )
    
    gen.save(get_output_path("custom_minimal.png"))
    print("   ✓ Saved: custom_minimal.png")


def example_5_abstract_art():
    """Create abstract art style post"""
    print("\n5. Creating abstract art design...")
    
    gen = PostGenerator()
    gen.create_canvas("square", (20, 20, 20))
    
    # Multiple gradient layers (create by regenerating canvas)
    # Base layer
    gen.apply_gradient((255, 50, 50), (50, 50, 255), "diagonal")
    
    # Add transparency overlay shapes in different positions
    gen.add_geometric_shapes("circles", (255, 255, 0), opacity=30, count=8)
    gen.add_geometric_shapes("rectangles", (0, 255, 255), opacity=25, count=10)
    gen.add_geometric_shapes("triangles", (255, 0, 255), opacity=20, count=7)
    
    # Cross-hatch pattern
    gen.add_pattern_lines((255, 255, 255), spacing=40, angle=45, width=1, opacity=20)
    gen.add_pattern_lines((255, 255, 255), spacing=40, angle=135, width=1, opacity=20)
    
    # Heavy vignette for focus
    gen.add_vignette(0.8)
    
    # Bold centered text
    gen.add_text(
        "ABSTRACT",
        position=(40, 480),
        font_size=90,
        color=(255, 255, 255),
        outline=True
    )
    
    gen.save(get_output_path("custom_abstract.png"))
    print("   ✓ Saved: custom_abstract.png")


def example_6_data_visualization_style():
    """Custom design for data/tech feel"""
    print("\n6. Creating data visualization style...")
    
    gen = PostGenerator()
    gen.create_canvas("horizontal", (5, 15, 35))
    
    # Tech gradient
    gen.apply_gradient((5, 15, 35), (10, 40, 80), "horizontal")
    
    # Grid pattern (multiple lines)
    for i in range(0, 1200, 100):
        gen.add_pattern_lines(
            color=(0, 150, 255),
            spacing=1200,  # Single line
            angle=90,
            width=1,
            opacity=30
        )
    
    # Horizontal grid lines
    gen.add_pattern_lines(
        color=(0, 150, 255),
        spacing=100,
        angle=0,
        width=1,
        opacity=20
    )
    
    # Tech circles
    gen.add_geometric_shapes("circles", (0, 200, 255), opacity=15, count=30)
    
    # Data-style text
    gen.add_text(
        "DATA DRIVEN",
        position=(50, 200),
        font_size=75,
        color=(0, 255, 255),
        shadow=True
    )
    
    gen.add_text_box(
        text="Revenue: +145%  |  Users: 2.5M  |  Growth: 98%",
        box_position=(50, 400),
        box_size=(1100, 120),
        bg_color=(0, 50, 100, 220),
        text_color=(255, 255, 255),
        font_size=32,
        padding=25
    )
    
    gen.save(get_output_path("custom_data_viz.png"))
    print("   ✓ Saved: custom_data_viz.png")


def example_7_neon_style():
    """Neon/cyberpunk style custom design"""
    print("\n7. Creating neon cyberpunk style...")
    
    gen = PostGenerator()
    gen.create_canvas("vertical", (10, 0, 20))
    
    # Dark purple gradient
    gen.apply_gradient((10, 0, 20), (50, 0, 80), "vertical")
    
    # Neon grid
    gen.add_pattern_lines((255, 0, 255), spacing=60, angle=0, width=2, opacity=40)
    gen.add_pattern_lines((0, 255, 255), spacing=60, angle=90, width=2, opacity=40)
    
    # Glowing circles
    gen.add_geometric_shapes("circles", (255, 0, 255), opacity=30, count=20)
    
    # Heavy vignette for neon effect
    gen.add_vignette(0.8)
    
    # Neon text (outline gives glow effect)
    gen.add_text(
        "NEON",
        position=(60, 500),
        font_size=130,
        color=(255, 0, 255),
        outline=True
    )
    
    gen.add_text(
        "FUTURE",
        position=(60, 670),
        font_size=130,
        color=(0, 255, 255),
        outline=True
    )
    
    gen.add_text(
        "Cyberpunk aesthetic with custom styling",
        position=(60, 900),
        font_size=38,
        color=(255, 100, 255),
        max_width=960
    )
    
    gen.save(get_output_path("custom_neon.png"))
    print("   ✓ Saved: custom_neon.png")


def example_8_magazine_cover():
    """Magazine cover style"""
    print("\n8. Creating magazine cover style...")
    
    gen = PostGenerator()
    gen.create_canvas("vertical", (255, 255, 255))
    
    # Bold color block
    gen.apply_gradient((220, 20, 60), (139, 0, 0), "diagonal")
    
    # Magazine style text box header
    gen.add_text_box(
        text="CUSTOM DESIGN MAGAZINE",
        box_position=(0, 0),
        box_size=(1080, 180),
        bg_color=(0, 0, 0, 255),
        text_color=(255, 215, 0),
        font_size=42,
        padding=40
    )
    
    # Main headline
    gen.add_text(
        "THE ART OF\nCUSTOM\nDESIGN",
        position=(60, 350),
        font_size=95,
        color=(255, 255, 255),
        max_width=960,
        shadow=True
    )
    
    # Subheading box
    gen.add_text_box(
        text="• Unlimited possibilities\n• Your vision, realized\n• Professional results",
        box_position=(60, 900),
        box_size=(960, 300),
        bg_color=(255, 255, 255, 240),
        text_color=(0, 0, 0),
        font_size=38,
        padding=40
    )
    
    gen.save(get_output_path("custom_magazine.png"))
    print("   ✓ Saved: custom_magazine.png")


def main():
    """Run all custom design examples"""
    print("=" * 60)
    print("  CUSTOM DESIGN EXAMPLES")
    print("=" * 60)
    print("\nGenerating 8 completely custom designs...")
    
    example_1_fully_custom()
    example_2_brand_colors()
    example_3_layered_effects()
    example_4_minimalist_custom()
    example_5_abstract_art()
    example_6_data_visualization_style()
    example_7_neon_style()
    example_8_magazine_cover()
    
    print("\n" + "=" * 60)
    print("✅ All custom designs generated!")
    print("\n📁 Generated files:")
    print("   • custom_design_1.png - Fully custom")
    print("   • custom_brand_colors.png - Brand colors")
    print("   • custom_layered.png - Layered effects")
    print("   • custom_minimal.png - Minimalist")
    print("   • custom_abstract.png - Abstract art")
    print("   • custom_data_viz.png - Data visualization")
    print("   • custom_neon.png - Neon cyberpunk")
    print("   • custom_magazine.png - Magazine cover")
    print("\n💡 These show you can create ANY design you want!")
    print("=" * 60)


if __name__ == "__main__":
    main()
