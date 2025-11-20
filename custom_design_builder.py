"""
Custom Design Builder
Interactive tool to create completely custom designs with full control
"""

import sys
import os

from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes


class CustomDesignBuilder:
    """
    Builder pattern for creating completely custom designs
    Provides a fluent API for maximum flexibility
    """
    
    def __init__(self):
        self.generator = PostGenerator()
        self.config = {
            'dimension': 'square',
            'background': (0, 0, 0),
            'gradient': None,
            'patterns': [],
            'effects': [],
            'texts': [],
            'logo': None,
        }
    
    def set_dimension(self, width, height=None):
        """Set custom dimension"""
        if height is None:
            # Preset dimension
            self.config['dimension'] = width
        else:
            # Custom size
            self.config['dimension'] = (width, height)
        return self
    
    def set_background(self, color):
        """Set background color (RGB tuple or hex string)"""
        if isinstance(color, str):
            color = self._hex_to_rgb(color)
        self.config['background'] = color
        return self
    
    def add_gradient(self, start_color, end_color, direction='vertical'):
        """Add gradient (can use RGB tuples or hex strings)"""
        if isinstance(start_color, str):
            start_color = self._hex_to_rgb(start_color)
        if isinstance(end_color, str):
            end_color = self._hex_to_rgb(end_color)
        
        self.config['gradient'] = {
            'start': start_color,
            'end': end_color,
            'direction': direction
        }
        return self
    
    def add_pattern_lines(self, color=(255, 255, 255), spacing=50, 
                         angle=45, width=2, opacity=30):
        """Add line pattern"""
        if isinstance(color, str):
            color = self._hex_to_rgb(color)
        
        self.config['patterns'].append({
            'type': 'lines',
            'color': color,
            'spacing': spacing,
            'angle': angle,
            'width': width,
            'opacity': opacity
        })
        return self
    
    def add_shapes(self, shape_type='circles', color=(255, 255, 255), 
                  opacity=20, count=10):
        """Add geometric shapes"""
        if isinstance(color, str):
            color = self._hex_to_rgb(color)
        
        self.config['patterns'].append({
            'type': 'shapes',
            'shape': shape_type,
            'color': color,
            'opacity': opacity,
            'count': count
        })
        return self
    
    def add_vignette(self, intensity=0.6):
        """Add vignette effect"""
        self.config['effects'].append({
            'type': 'vignette',
            'intensity': intensity
        })
        return self
    
    def add_noise(self, intensity=10):
        """Add noise texture"""
        self.config['effects'].append({
            'type': 'noise',
            'intensity': intensity
        })
        return self
    
    def add_blur(self, radius=5, region=None):
        """Add blur effect"""
        self.config['effects'].append({
            'type': 'blur',
            'radius': radius,
            'region': region
        })
        return self
    
    def add_text(self, text, x, y, font_size=70, color=(255, 255, 255),
                max_width=None, shadow=False, outline=False,
                font_path="fonts/Poppins-Bold.ttf"):
        """Add text element"""
        if isinstance(color, str):
            color = self._hex_to_rgb(color)
        
        self.config['texts'].append({
            'text': text,
            'position': (x, y),
            'font_size': font_size,
            'color': color,
            'max_width': max_width,
            'shadow': shadow,
            'outline': outline,
            'font_path': font_path
        })
        return self
    
    def add_text_box(self, text, x, y, width, height, 
                    bg_color=(0, 0, 0, 180), text_color=(255, 255, 255),
                    font_size=40, padding=20):
        """Add text box with background"""
        if isinstance(text_color, str):
            text_color = self._hex_to_rgb(text_color)
        
        self.config['texts'].append({
            'type': 'textbox',
            'text': text,
            'box_position': (x, y),
            'box_size': (width, height),
            'bg_color': bg_color,
            'text_color': text_color,
            'font_size': font_size,
            'padding': padding
        })
        return self
    
    def add_logo(self, logo_path, position='top-left', size=(200, 200), margin=40):
        """Add logo"""
        self.config['logo'] = {
            'path': logo_path,
            'position': position,
            'size': size,
            'margin': margin
        }
        return self
    
    def build(self, output_path='output/custom_design.png'):
        """Build the design and save to file"""
        # Create canvas
        self.generator.create_canvas(
            self.config['dimension'],
            self.config['background']
        )
        
        # Apply gradient
        if self.config['gradient']:
            g = self.config['gradient']
            self.generator.apply_gradient(
                g['start'], g['end'], g['direction']
            )
        
        # Apply patterns
        for pattern in self.config['patterns']:
            if pattern['type'] == 'lines':
                self.generator.add_pattern_lines(
                    pattern['color'],
                    pattern['spacing'],
                    pattern['angle'],
                    pattern['width'],
                    pattern['opacity']
                )
            elif pattern['type'] == 'shapes':
                self.generator.add_geometric_shapes(
                    pattern['shape'],
                    pattern['color'],
                    pattern['opacity'],
                    pattern['count']
                )
        
        # Apply effects
        for effect in self.config['effects']:
            if effect['type'] == 'vignette':
                self.generator.add_vignette(effect['intensity'])
            elif effect['type'] == 'noise':
                self.generator.add_noise(effect['intensity'])
            elif effect['type'] == 'blur':
                self.generator.add_blur(effect['radius'], effect.get('region'))
        
        # Add logo
        if self.config['logo']:
            logo = self.config['logo']
            self.generator.add_logo(
                logo['path'],
                logo['position'],
                logo['size'],
                logo['margin']
            )
        
        # Add texts
        for text_config in self.config['texts']:
            if text_config.get('type') == 'textbox':
                self.generator.add_text_box(
                    text_config['text'],
                    text_config['box_position'],
                    text_config['box_size'],
                    text_config['bg_color'],
                    text_config['text_color'],
                    text_config.get('font_path', 'fonts/Poppins-Regular.ttf'),
                    text_config['font_size'],
                    text_config['padding']
                )
            else:
                self.generator.add_text(
                    text_config['text'],
                    text_config['position'],
                    text_config.get('font_path', 'fonts/Poppins-Bold.ttf'),
                    text_config['font_size'],
                    text_config['color'],
                    text_config['max_width'],
                    text_config.get('align', 'left'),
                    text_config['shadow'],
                    text_config['outline']
                )
        
        # Save
        self.generator.save(output_path)
        return output_path
    
    def preview(self):
        """Show preview without saving"""
        self.generator.show()
        return self
    
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


# Example usage functions
def example_fluent_api():
    """Example using fluent API"""
    print("Creating design with fluent API...")
    
    design = CustomDesignBuilder()
    
    design \
        .set_dimension('square') \
        .set_background('#000000') \
        .add_gradient('#8B00FF', '#FF1493', 'diagonal') \
        .add_pattern_lines('#FFFFFF', spacing=60, angle=45, opacity=25) \
        .add_shapes('circles', '#FFD700', opacity=20, count=15) \
        .add_vignette(0.6) \
        .add_noise(8) \
        .add_text('FLUENT API', 40, 400, font_size=90, color='#FFFFFF', shadow=True) \
        .add_text('Chain methods for easy building', 40, 550, font_size=40, color='#FFD700') \
        .build('output/custom_fluent_api.png')
    
    print("✓ Saved: output/custom_fluent_api.png")


def example_brand_design():
    """Example creating a brand design"""
    print("Creating custom brand design...")
    
    # Your brand colors
    BRAND = {
        'primary': '#0066CC',
        'secondary': '#FF6600',
        'accent': '#00CC99',
        'dark': '#14142A'
    }
    
    design = CustomDesignBuilder()
    
    design \
        .set_dimension(1200, 1200) \
        .set_background(BRAND['dark']) \
        .add_gradient(BRAND['primary'], BRAND['dark'], 'radial') \
        .add_pattern_lines(BRAND['accent'], spacing=70, angle=30, opacity=30) \
        .add_pattern_lines(BRAND['accent'], spacing=70, angle=150, opacity=30) \
        .add_vignette(0.5) \
        .add_text('YOUR BRAND', 60, 450, font_size=95, color='#FFFFFF', outline=True) \
        .add_text('YOUR STYLE', 60, 580, font_size=95, color=BRAND['secondary'], shadow=True) \
        .add_text_box(
            'Custom colors • Custom layout • Your identity',
            60, 850, 1080, 200,
            bg_color=(0, 0, 0, 200),
            text_color=(255, 255, 255),
            font_size=38
        ) \
        .build('output/custom_brand_builder.png')
    
    print("✓ Saved: output/custom_brand_builder.png")


def example_minimalist():
    """Example creating minimalist design"""
    print("Creating minimalist custom design...")
    
    design = CustomDesignBuilder()
    
    design \
        .set_dimension('square') \
        .set_background('#FAFAFA') \
        .add_gradient('#FAFAFA', '#F0F0F5', 'vertical') \
        .add_text('MINIMAL', 40, 40, font_size=50, color='#333333') \
        .add_text('Design', 40, 480, font_size=100, color='#1A1A1A') \
        .add_text('Sometimes less is more', 40, 640, font_size=35, color='#999999') \
        .build('output/custom_minimal_builder.png')
    
    print("✓ Saved: output/custom_minimal_builder.png")


def main():
    """Run custom design builder examples"""
    print("=" * 60)
    print("  CUSTOM DESIGN BUILDER EXAMPLES")
    print("=" * 60)
    print("\nShowing how to build completely custom designs...\n")
    
    example_fluent_api()
    example_brand_design()
    example_minimalist()
    
    print("\n" + "=" * 60)
    print("✅ Custom designs created with builder!")
    print("\n💡 The Builder Pattern gives you:")
    print("   • Fluent, chainable API")
    print("   • Full control over every element")
    print("   • Clean, readable code")
    print("   • Hex color support (#RRGGBB)")
    print("   • Any dimension, any style")
    print("\n📁 Files created:")
    print("   • output/custom_fluent_api.png")
    print("   • output/custom_brand_builder.png")
    print("   • output/custom_minimal_builder.png")
    print("=" * 60)


if __name__ == "__main__":
    main()
