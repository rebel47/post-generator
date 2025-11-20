"""
Demo script - Generates multiple sample posts showcasing all features
Run this to see what the system can do!
"""

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes
from post_generator.template_loader import TemplateLoader
import os

def create_demo_posts():
    """Generate a showcase of different post styles"""
    
    print("🎨 Post Generator Demo")
    print("=" * 60)
    print("\nGenerating sample posts to showcase features...\n")
    
    # Ensure output directory exists
    os.makedirs("output/demo", exist_ok=True)
    
    # Create default templates
    print("📋 Creating templates...")
    loader = TemplateLoader()
    loader.create_default_templates()
    
    demos = []
    
    # Demo 1: Simple gradient
    print("\n1. Simple Gradient Post...")
    gen = PostGenerator()
    gen.create_canvas("square", (0, 0, 0))
    gen.apply_gradient((255, 0, 0), (0, 0, 0), "vertical")
    gen.add_text("Simple & Elegant", (40, 450), font_size=75, color=(255, 255, 255), shadow=True)
    gen.save("output/demo/01_simple_gradient.png")
    demos.append("01_simple_gradient.png")
    
    # Demo 2: Diagonal lines
    print("2. Diagonal Lines Pattern...")
    gen = PostGenerator()
    scheme = ColorSchemes.BOLD_RED
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "diagonal")
    gen.add_pattern_lines(scheme.get_accent_rgb(), spacing=60, angle=45)
    gen.add_vignette(0.5)
    gen.add_text("Bold Design", (40, 450), font_size=80, color=(255, 255, 255), outline=True)
    gen.save("output/demo/02_bold_lines.png")
    demos.append("02_bold_lines.png")
    
    # Demo 3: Geometric shapes
    print("3. Geometric Shapes...")
    gen = PostGenerator()
    scheme = ColorSchemes.GRADIENT_OCEAN
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "radial")
    gen.add_geometric_shapes("circles", (255, 255, 255), opacity=20, count=20)
    gen.add_text("Creative Vision", (40, 450), font_size=75, color=(255, 255, 255), shadow=True)
    gen.save("output/demo/03_geometric.png")
    demos.append("03_geometric.png")
    
    # Demo 4: Minimal clean
    print("4. Minimal Clean Design...")
    gen = PostGenerator()
    scheme = ColorSchemes.MINIMAL_GRAY
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.add_text("Less is More", (40, 400), font_size=70, color=scheme.get_text_rgb())
    gen.add_text("Minimalist Approach", (40, 550), font_size=40, color=scheme.get_accent_rgb())
    gen.save("output/demo/04_minimal.png")
    demos.append("04_minimal.png")
    
    # Demo 5: Text box
    print("5. Text Box Design...")
    gen = PostGenerator()
    scheme = ColorSchemes.CORPORATE_TECH
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "vertical")
    gen.add_text("Q4 Results", (40, 300), font_size=80, color=(255, 255, 255), shadow=True)
    gen.add_text_box(
        "Revenue: $10M\nGrowth: 45%\nCustomers: 50K+",
        (40, 650), (1000, 280),
        bg_color=(0, 0, 0, 200),
        font_size=38
    )
    gen.save("output/demo/05_textbox.png")
    demos.append("05_textbox.png")
    
    # Demo 6: Purple modern
    print("6. Purple Modern...")
    gen = PostGenerator()
    scheme = ColorSchemes.BOLD_PURPLE
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "vertical")
    gen.add_noise(intensity=10)
    gen.add_text("Modern\nInnovation", (40, 380), font_size=90, 
                color=(255, 255, 255), max_width=900, shadow=True)
    gen.save("output/demo/06_purple_modern.png")
    demos.append("06_purple_modern.png")
    
    # Demo 7: Sunset gradient
    print("7. Sunset Gradient...")
    gen = PostGenerator()
    scheme = ColorSchemes.GRADIENT_SUNSET
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "diagonal")
    gen.add_vignette(0.6)
    gen.add_text("Sunset Vibes", (40, 450), font_size=75, color=(255, 255, 255), outline=True)
    gen.save("output/demo/07_sunset.png")
    demos.append("07_sunset.png")
    
    # Demo 8: Professional vertical (story)
    print("8. Professional Story Format...")
    gen = PostGenerator()
    scheme = ColorSchemes.PROFESSIONAL_BLUE
    gen.create_canvas("story", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "vertical")
    gen.add_vignette(0.4)
    gen.add_text("LinkedIn\nStory", (60, 700), font_size=110, 
                color=(255, 255, 255), max_width=960, shadow=True)
    gen.add_text("Swipe up to learn more", (60, 1100), font_size=45, 
                color=scheme.get_accent_rgb(), max_width=960)
    gen.save("output/demo/08_story.png")
    demos.append("08_story.png")
    
    # Demo 9: Forest minimal
    print("9. Forest Minimal...")
    gen = PostGenerator()
    scheme = ColorSchemes.GRADIENT_FOREST
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "horizontal")
    gen.add_noise(5)
    gen.add_text("Nature\nInspired", (40, 400), font_size=80, 
                color=(255, 255, 255), max_width=900, shadow=True)
    gen.save("output/demo/09_forest.png")
    demos.append("09_forest.png")
    
    # Demo 10: Orange energy
    print("10. Orange Energy...")
    gen = PostGenerator()
    scheme = ColorSchemes.BOLD_ORANGE
    gen.create_canvas("square", scheme.get_background_rgb())
    gen.apply_gradient(scheme.get_primary_rgb(), scheme.get_secondary_rgb(), "radial")
    gen.add_pattern_lines((255, 255, 255), spacing=70, angle=135, opacity=25)
    gen.add_text("High Energy", (40, 450), font_size=80, color=(255, 255, 255), outline=True)
    gen.save("output/demo/10_orange_energy.png")
    demos.append("10_orange_energy.png")
    
    print("\n" + "=" * 60)
    print("\n✅ Demo Complete!")
    print(f"\n📁 Generated {len(demos)} sample posts in: output/demo/")
    print("\n📋 Generated files:")
    for demo in demos:
        print(f"   • {demo}")
    
    print("\n🎨 Features Demonstrated:")
    print("   ✓ Vertical, horizontal, diagonal, and radial gradients")
    print("   ✓ Pattern overlays (lines, geometric shapes)")
    print("   ✓ Effects (vignette, noise, shadows, outlines)")
    print("   ✓ Multiple dimensions (square, story)")
    print("   ✓ Text boxes with backgrounds")
    print("   ✓ 10 different color schemes")
    
    print("\n🚀 Try It Yourself:")
    print("   • Modify the code above")
    print("   • Check examples/ directory for more")
    print("   • Use CLI: python cli.py --help")
    print("   • Read README.md for full documentation")


if __name__ == "__main__":
    create_demo_posts()
