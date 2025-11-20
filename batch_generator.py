"""
Batch Post Generator
Generate multiple posts from CSV or JSON data files
"""

import csv
import json
import os
from typing import List, Dict, Any, Optional
from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes
from post_generator.template_loader import TemplateLoader


class BatchGenerator:
    """Generate multiple posts from data files"""
    
    def __init__(self, output_dir: str = "output/batch"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.generator = PostGenerator()
    
    def generate_from_csv(self, csv_path: str, logo_path: Optional[str] = None) -> List[str]:
        """
        Generate posts from CSV file
        
        CSV format:
        template,text,subtext,output_filename
        
        Example:
        professional_gradient,"Innovation starts here","Join us today",post1.png
        bold_red_lines,"New Product Launch","Available Now",post2.png
        """
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        
        generated_files = []
        
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for i, row in enumerate(reader, 1):
                try:
                    output_filename = row.get('output_filename', f'post_{i}.png')
                    output_path = os.path.join(self.output_dir, output_filename)
                    
                    template_name = row.get('template')
                    text = row.get('text', '')
                    subtext = row.get('subtext')
                    
                    if template_name:
                        self._generate_from_template(
                            template_name, text, subtext, logo_path, output_path
                        )
                    else:
                        # Custom generation from CSV columns
                        self._generate_custom(row, logo_path, output_path)
                    
                    generated_files.append(output_path)
                    print(f"✓ Generated: {output_path}")
                
                except Exception as e:
                    print(f"✗ Error generating post {i}: {e}")
        
        print(f"\n✓ Batch complete: {len(generated_files)} posts generated")
        return generated_files
    
    def generate_from_json(self, json_path: str, logo_path: Optional[str] = None) -> List[str]:
        """
        Generate posts from JSON file
        
        JSON format:
        [
          {
            "template": "professional_gradient",
            "text": "Innovation starts here",
            "subtext": "Join us today",
            "output_filename": "post1.png"
          },
          ...
        ]
        """
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"JSON file not found: {json_path}")
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            raise ValueError("JSON must contain an array of post definitions")
        
        generated_files = []
        
        for i, post_data in enumerate(data, 1):
            try:
                output_filename = post_data.get('output_filename', f'post_{i}.png')
                output_path = os.path.join(self.output_dir, output_filename)
                
                template_name = post_data.get('template')
                text = post_data.get('text', '')
                subtext = post_data.get('subtext')
                post_logo = post_data.get('logo', logo_path)
                
                if template_name:
                    self._generate_from_template(
                        template_name, text, subtext, post_logo, output_path
                    )
                else:
                    self._generate_custom(post_data, post_logo, output_path)
                
                generated_files.append(output_path)
                print(f"✓ Generated: {output_path}")
            
            except Exception as e:
                print(f"✗ Error generating post {i}: {e}")
        
        print(f"\n✓ Batch complete: {len(generated_files)} posts generated")
        return generated_files
    
    def _generate_from_template(self, template_name: str, text: str, 
                                subtext: Optional[str], logo_path: Optional[str],
                                output_path: str):
        """Generate a post using a template"""
        loader = TemplateLoader()
        template = loader.load_template(template_name)
        color_scheme = ColorSchemes.get_scheme(template.color_scheme)
        
        # Create canvas
        self.generator.create_canvas(template.dimension, color_scheme.get_background_rgb())
        
        # Apply background
        if template.background_type == "gradient":
            self.generator.apply_gradient(
                color_scheme.get_primary_rgb(),
                color_scheme.get_secondary_rgb(),
                template.gradient_direction
            )
        
        # Add patterns
        if template.pattern_type:
            if template.pattern_type == "lines":
                self.generator.add_pattern_lines(
                    color_scheme.get_accent_rgb(),
                    spacing=template.pattern_spacing,
                    angle=template.pattern_angle
                )
            else:
                self.generator.add_geometric_shapes(
                    template.pattern_type,
                    color_scheme.get_accent_rgb()
                )
        
        # Add effects
        if template.add_vignette:
            self.generator.add_vignette(template.vignette_intensity)
        if template.add_noise:
            self.generator.add_noise(template.noise_intensity)
        
        # Add logo
        if logo_path:
            self.generator.add_logo(
                logo_path,
                position=template.logo_position,
                size=template.logo_size,
                margin=template.logo_margin
            )
        
        # Add text
        self.generator.add_text(
            text,
            position=tuple(template.headline_position),
            font_size=template.headline_size,
            color=color_scheme.get_text_rgb(),
            max_width=template.headline_max_width,
            shadow=template.headline_shadow,
            outline=template.headline_outline
        )
        
        # Add subtext
        if subtext and template.has_subheadline:
            self.generator.add_text(
                subtext,
                position=tuple(template.subheadline_position),
                font_path=template.subheadline_font,
                font_size=template.subheadline_size,
                color=color_scheme.get_text_rgb(),
                max_width=template.subheadline_max_width
            )
        
        # Save
        self.generator.save(output_path)
    
    def _generate_custom(self, config: Dict[str, Any], logo_path: Optional[str],
                        output_path: str):
        """Generate a post with custom configuration"""
        # Get configuration
        dimension = config.get('dimension', 'square')
        color_scheme_name = config.get('color_scheme', 'professional_dark')
        text = config.get('text', '')
        subtext = config.get('subtext')
        
        # Get color scheme
        color_scheme = ColorSchemes.get_scheme(color_scheme_name)
        
        # Create canvas
        self.generator.create_canvas(dimension, color_scheme.get_background_rgb())
        
        # Apply gradient if specified
        gradient_direction = config.get('gradient_direction', 'vertical')
        self.generator.apply_gradient(
            color_scheme.get_primary_rgb(),
            color_scheme.get_secondary_rgb(),
            gradient_direction
        )
        
        # Add effects
        if config.get('add_vignette', False):
            self.generator.add_vignette()
        if config.get('add_noise', False):
            self.generator.add_noise()
        
        # Add logo
        if logo_path:
            logo_position = config.get('logo_position', 'top-left')
            self.generator.add_logo(logo_path, position=logo_position)
        
        # Add text
        font_size = config.get('font_size', 70)
        text_position = config.get('text_position', [40, 400])
        
        self.generator.add_text(
            text,
            position=tuple(text_position),
            font_size=font_size,
            color=color_scheme.get_text_rgb(),
            max_width=900
        )
        
        # Add subtext
        if subtext:
            subtext_position = config.get('subtext_position', [40, 550])
            self.generator.add_text(
                subtext,
                position=tuple(subtext_position),
                font_size=40,
                color=color_scheme.get_text_rgb(),
                max_width=900
            )
        
        # Save
        self.generator.save(output_path)
    
    def create_sample_csv(self, output_path: str = "sample_posts.csv"):
        """Create a sample CSV file for batch generation"""
        sample_data = [
            {
                'template': 'professional_gradient',
                'text': 'Innovation Starts Here',
                'subtext': 'Join the future of technology',
                'output_filename': 'post_innovation.png'
            },
            {
                'template': 'bold_red_lines',
                'text': 'New Product Launch',
                'subtext': 'Available Now',
                'output_filename': 'post_launch.png'
            },
            {
                'template': 'minimal_clean',
                'text': 'Simplicity is Key',
                'subtext': 'Less is More',
                'output_filename': 'post_minimal.png'
            },
        ]
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['template', 'text', 'subtext', 'output_filename'])
            writer.writeheader()
            writer.writerows(sample_data)
        
        print(f"✓ Created sample CSV: {output_path}")
    
    def create_sample_json(self, output_path: str = "sample_posts.json"):
        """Create a sample JSON file for batch generation"""
        sample_data = [
            {
                "template": "professional_gradient",
                "text": "Innovation Starts Here",
                "subtext": "Join the future of technology",
                "output_filename": "post_innovation.png"
            },
            {
                "template": "bold_red_lines",
                "text": "New Product Launch",
                "subtext": "Available Now",
                "output_filename": "post_launch.png"
            },
            {
                "template": "minimal_clean",
                "text": "Simplicity is Key",
                "subtext": "Less is More",
                "output_filename": "post_minimal.png"
            },
        ]
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, indent=2)
        
        print(f"✓ Created sample JSON: {output_path}")


def main():
    """CLI for batch generation"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Batch Post Generator")
    parser.add_argument('--csv', help='Path to CSV file')
    parser.add_argument('--json', help='Path to JSON file')
    parser.add_argument('--logo', help='Path to logo file (optional)')
    parser.add_argument('--output-dir', default='output/batch', help='Output directory')
    parser.add_argument('--create-sample-csv', action='store_true', help='Create sample CSV file')
    parser.add_argument('--create-sample-json', action='store_true', help='Create sample JSON file')
    
    args = parser.parse_args()
    
    batch = BatchGenerator(args.output_dir)
    
    if args.create_sample_csv:
        batch.create_sample_csv()
        return
    
    if args.create_sample_json:
        batch.create_sample_json()
        return
    
    if args.csv:
        batch.generate_from_csv(args.csv, args.logo)
    elif args.json:
        batch.generate_from_json(args.json, args.logo)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
