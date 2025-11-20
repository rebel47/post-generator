"""
Test script to verify installation and generate a sample post
"""

import sys
import os

def test_installation():
    """Test if all components are working"""
    
    print("🧪 Testing Post Generator Installation\n")
    print("=" * 60)
    
    # Test 1: Import core modules
    print("\n1. Testing imports...")
    try:
        from post_generator import PostGenerator
        from post_generator.color_schemes import ColorSchemes
        from post_generator.template_loader import TemplateLoader
        from post_generator.typography import Typography
        print("   ✓ All modules imported successfully")
    except ImportError as e:
        print(f"   ✗ Import error: {e}")
        print("   → Run: pip install -r requirements.txt")
        return False
    
    # Test 2: Check PIL/Pillow
    print("\n2. Testing Pillow (PIL)...")
    try:
        from PIL import Image, ImageDraw, ImageFont
        print("   ✓ Pillow is installed")
    except ImportError:
        print("   ✗ Pillow not found")
        print("   → Run: pip install Pillow")
        return False
    
    # Test 3: Create directories
    print("\n3. Testing directory structure...")
    try:
        os.makedirs("output", exist_ok=True)
        os.makedirs("templates", exist_ok=True)
        print("   ✓ Directories created/verified")
    except Exception as e:
        print(f"   ✗ Directory error: {e}")
        return False
    
    # Test 4: Create default templates
    print("\n4. Creating default templates...")
    try:
        loader = TemplateLoader()
        loader.create_default_templates()
        templates = loader.list_templates()
        print(f"   ✓ Created {len(templates)} templates")
    except Exception as e:
        print(f"   ✗ Template error: {e}")
        return False
    
    # Test 5: List color schemes
    print("\n5. Testing color schemes...")
    try:
        schemes = ColorSchemes.list_schemes()
        print(f"   ✓ Found {len(schemes)} color schemes")
    except Exception as e:
        print(f"   ✗ Color scheme error: {e}")
        return False
    
    # Test 6: Generate a test post
    print("\n6. Generating test post...")
    try:
        generator = PostGenerator()
        
        # Create a simple test post
        generator.create_canvas("square", color=(0, 0, 0))
        generator.apply_gradient(
            start_color=(50, 50, 150),
            end_color=(0, 0, 0),
            direction="vertical"
        )
        generator.add_text(
            "Installation Test",
            position=(40, 400),
            font_size=60,
            color=(255, 255, 255),
            shadow=True
        )
        generator.add_text(
            "System is working! ✓",
            position=(40, 550),
            font_size=40,
            color=(100, 255, 100)
        )
        
        output_path = "output/test_post.png"
        generator.save(output_path)
        print(f"   ✓ Test post saved: {output_path}")
    except Exception as e:
        print(f"   ✗ Generation error: {e}")
        return False
    
    # Test 7: Check optional dependencies
    print("\n7. Checking optional dependencies...")
    
    # FastAPI
    try:
        import fastapi
        import uvicorn
        print("   ✓ FastAPI available (API enabled)")
    except ImportError:
        print("   ⚠ FastAPI not installed (API disabled)")
        print("   → To enable API: pip install fastapi uvicorn python-multipart")
    
    print("\n" + "=" * 60)
    print("\n✅ All core tests passed!")
    print("\n📋 Summary:")
    print(f"   • Templates: {len(templates)} available")
    print(f"   • Color Schemes: {len(schemes)} available")
    print(f"   • Test Post: output/test_post.png")
    print("\n🚀 Ready to generate posts!")
    print("\n📖 Next steps:")
    print("   1. Run examples: python examples/example_basic.py")
    print("   2. Try CLI: python cli.py --list-templates")
    print("   3. Read QUICKSTART.md for more info")
    
    return True


if __name__ == "__main__":
    success = test_installation()
    sys.exit(0 if success else 1)
