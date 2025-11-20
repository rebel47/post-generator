"""
Command Line Interface for Post Generator
Provides easy command-line access to generate posts
"""

import argparse
import sys
import os
from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes
from post_generator.template_loader import TemplateLoader


def main():
    parser = argparse.ArgumentParser(
        description="LinkedIn-style Post Generator - Create branded social media posts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate from template
  python cli.py --template professional_gradient --text "Innovation starts here" --logo logo.png
  
  # Custom post with gradient
  python cli.py --text "Hello World" --gradient-start "#000000" --gradient-end "#FF0000"
  
  # List available templates
  python cli.py --list-templates
  
  # List color schemes
  python cli.py --list-colors
        """
    )
    
    # Template options
    parser.add_argument('--template', '-t', help='Template name to use')
    parser.add_argument('--list-templates', action='store_true', help='List available templates')
    parser.add_argument('--create-defaults', action='store_true', help='Create default templates')
    
    # Content options
    parser.add_argument('--text', help='Main headline text')
    parser.add_argument('--subtext', help='Subheadline text')
    parser.add_argument('--logo', help='Path to logo file')
    
    # Dimension options
    parser.add_argument('--dimension', '-d', default='square',
                       choices=['square', 'square_large', 'vertical', 'story', 
                               'horizontal', 'linkedin_banner', 'twitter_post'],
                       help='Post dimensions (default: square)')
    parser.add_argument('--custom-size', help='Custom size as WIDTHxHEIGHT (e.g., 1080x1080)')
    
    # Background options
    parser.add_argument('--bg-color', help='Background color (hex, e.g., #000000)')
    parser.add_argument('--gradient-start', help='Gradient start color (hex)')
    parser.add_argument('--gradient-end', help='Gradient end color (hex)')
    parser.add_argument('--gradient-direction', choices=['vertical', 'horizontal', 'diagonal', 'radial'],
                       default='vertical', help='Gradient direction')
    
    # Color scheme
    parser.add_argument('--color-scheme', '-c', help='Color scheme name')
    parser.add_argument('--list-colors', action='store_true', help='List available color schemes')
    
    # Pattern options
    parser.add_argument('--pattern', choices=['lines', 'circles', 'rectangles', 'triangles'],
                       help='Add pattern overlay')
    parser.add_argument('--pattern-angle', type=int, default=45, help='Pattern angle (for lines)')
    parser.add_argument('--pattern-spacing', type=int, default=50, help='Pattern spacing')
    
    # Effects
    parser.add_argument('--vignette', action='store_true', help='Add vignette effect')
    parser.add_argument('--noise', action='store_true', help='Add noise texture')
    parser.add_argument('--shadow', action='store_true', help='Add text shadow')
    parser.add_argument('--outline', action='store_true', help='Add text outline')
    
    # Logo options
    parser.add_argument('--logo-position', default='top-left',
                       choices=['top-left', 'top-center', 'top-right', 
                               'bottom-left', 'bottom-center', 'bottom-right', 'center'],
                       help='Logo position')
    parser.add_argument('--logo-size', help='Logo size as WIDTHxHEIGHT (e.g., 200x200)')
    
    # Text options
    parser.add_argument('--font-size', type=int, default=70, help='Headline font size')
    parser.add_argument('--text-color', default='#FFFFFF', help='Text color (hex)')
    parser.add_argument('--text-position', help='Text position as X,Y (e.g., 40,400)')
    
    # Output options
    parser.add_argument('--output', '-o', default='output/post.png', help='Output file path')
    parser.add_argument('--show', action='store_true', help='Display the image after generation')
    
    args = parser.parse_args()
    
    # Handle list commands
    if args.list_templates:
        loader = TemplateLoader()
        templates = loader.list_templates()
        if templates:
            print("Available templates:")
            for t in templates:
                print(f"  - {t}")
        else:
            print("No templates found. Run with --create-defaults to create them.")
        return
    
    if args.list_colors:
        schemes = ColorSchemes.list_schemes()
        print("Available color schemes:")
        for s in schemes:
            print(f"  - {s}")
        return
    
    if args.create_defaults:
        loader = TemplateLoader()
        loader.create_default_templates()
        return
    
    # Generate post
    if not args.text and not args.template:
        parser.error("Either --text or --template is required")
    
    try:
        generator = PostGenerator()
        
        # Use template if provided
        if args.template:
            loader = TemplateLoader()
            template = loader.load_template(args.template)
            
            # Get color scheme
            color_scheme = ColorSchemes.get_scheme(template.color_scheme)
            
            # Create canvas
            dimension = args.custom_size.split('x') if args.custom_size else template.dimension
            if isinstance(dimension, list):
                dimension = (int(dimension[0]), int(dimension[1]))
            
            generator.create_canvas(dimension, color_scheme.get_background_rgb())
            
            # Apply background
            if template.background_type == "gradient":
                generator.apply_gradient(
                    color_scheme.get_primary_rgb(),
                    color_scheme.get_secondary_rgb(),
                    template.gradient_direction
                )
            
            # Add patterns
            if template.pattern_type:
                if template.pattern_type == "lines":
                    generator.add_pattern_lines(
                        color_scheme.get_accent_rgb(),
                        spacing=template.pattern_spacing,
                        angle=template.pattern_angle
                    )
                else:
                    generator.add_geometric_shapes(
                        template.pattern_type,
                        color_scheme.get_accent_rgb()
                    )
            
            # Add effects
            if template.add_vignette:
                generator.add_vignette(template.vignette_intensity)
            if template.add_noise:
                generator.add_noise(template.noise_intensity)
            
            # Add logo
            if args.logo:
                logo_size = tuple(map(int, args.logo_size.split('x'))) if args.logo_size else template.logo_size
                generator.add_logo(
                    args.logo,
                    position=args.logo_position if args.logo_position != 'top-left' else template.logo_position,
                    size=logo_size,
                    margin=template.logo_margin
                )
            
            # Add text
            text = args.text if args.text else "Your Headline Here"
            text_color = hex_to_rgb(args.text_color) if args.text_color else color_scheme.get_text_rgb()
            
            generator.add_text(
                text,
                position=tuple(template.headline_position),
                font_size=args.font_size if args.font_size != 70 else template.headline_size,
                color=text_color,
                max_width=template.headline_max_width,
                shadow=template.headline_shadow or args.shadow,
                outline=template.headline_outline or args.outline
            )
            
            # Add subtext if provided
            if args.subtext and template.has_subheadline:
                generator.add_text(
                    args.subtext,
                    position=tuple(template.subheadline_position),
                    font_path=template.subheadline_font,
                    font_size=template.subheadline_size,
                    color=text_color,
                    max_width=template.subheadline_max_width
                )
        
        else:
            # Manual generation without template
            dimension = args.custom_size.split('x') if args.custom_size else args.dimension
            if isinstance(dimension, list):
                dimension = (int(dimension[0]), int(dimension[1]))
            
            # Determine background color
            bg_color = (0, 0, 0)
            if args.bg_color:
                bg_color = hex_to_rgb(args.bg_color)
            elif args.color_scheme:
                scheme = ColorSchemes.get_scheme(args.color_scheme)
                bg_color = scheme.get_background_rgb()
            
            generator.create_canvas(dimension, bg_color)
            
            # Apply gradient
            if args.gradient_start and args.gradient_end:
                start = hex_to_rgb(args.gradient_start)
                end = hex_to_rgb(args.gradient_end)
                generator.apply_gradient(start, end, args.gradient_direction)
            
            # Add pattern
            if args.pattern:
                if args.pattern == 'lines':
                    generator.add_pattern_lines(
                        spacing=args.pattern_spacing,
                        angle=args.pattern_angle
                    )
                else:
                    generator.add_geometric_shapes(args.pattern)
            
            # Add effects
            if args.vignette:
                generator.add_vignette()
            if args.noise:
                generator.add_noise()
            
            # Add logo
            if args.logo:
                logo_size = tuple(map(int, args.logo_size.split('x'))) if args.logo_size else (200, 200)
                generator.add_logo(args.logo, position=args.logo_position, size=logo_size)
            
            # Add text
            text_pos = tuple(map(int, args.text_position.split(','))) if args.text_position else (40, 400)
            text_color = hex_to_rgb(args.text_color)
            
            generator.add_text(
                args.text,
                position=text_pos,
                font_size=args.font_size,
                color=text_color,
                max_width=900,
                shadow=args.shadow,
                outline=args.outline
            )
            
            # Add subtext
            if args.subtext:
                subtext_pos = (text_pos[0], text_pos[1] + 150)
                generator.add_text(
                    args.subtext,
                    position=subtext_pos,
                    font_size=40,
                    color=text_color,
                    max_width=900
                )
        
        # Save
        generator.save(args.output)
        
        # Show if requested
        if args.show:
            generator.show()
        
        print(f"\n✓ Success! Post saved to: {args.output}")
    
    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    main()
