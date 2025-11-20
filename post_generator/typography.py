"""
Typography Manager for Post Generator
Handles text rendering, wrapping, and font management
"""

from typing import Tuple, List, Optional
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


class Typography:
    """Manages typography for post generation"""
    
    # Default font paths (will try to use system fonts if custom not available)
    DEFAULT_FONTS = {
        "bold": "fonts/Poppins-Bold.ttf",
        "semibold": "fonts/Poppins-SemiBold.ttf",
        "regular": "fonts/Poppins-Regular.ttf",
        "light": "fonts/Poppins-Light.ttf",
    }
    
    # Fallback to system fonts if custom fonts not available
    SYSTEM_FONT_FALLBACKS = {
        "Windows": "arial.ttf",
        "Linux": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "Darwin": "/System/Library/Fonts/Helvetica.ttc",  # macOS
    }
    
    def __init__(self, base_path: str = "."):
        self.base_path = base_path
        self.font_cache = {}
    
    def get_font(self, font_path: str, size: int) -> ImageFont.FreeTypeFont:
        """Get a font with caching"""
        cache_key = f"{font_path}_{size}"
        
        if cache_key in self.font_cache:
            return self.font_cache[cache_key]
        
        # Try custom font first
        full_path = os.path.join(self.base_path, font_path)
        
        try:
            if os.path.exists(full_path):
                font = ImageFont.truetype(full_path, size)
            else:
                # Try system font
                import platform
                system = platform.system()
                fallback = self.SYSTEM_FONT_FALLBACKS.get(system, "arial.ttf")
                try:
                    font = ImageFont.truetype(fallback, size)
                except:
                    # Last resort: default PIL font
                    font = ImageFont.load_default()
            
            self.font_cache[cache_key] = font
            return font
        
        except Exception as e:
            print(f"Warning: Could not load font {font_path}, using default. Error: {e}")
            return ImageFont.load_default()
    
    def wrap_text(self, text: str, font: ImageFont.FreeTypeFont, max_width: int, 
                  draw: ImageDraw.Draw) -> List[str]:
        """Wrap text to fit within max_width"""
        lines = []
        words = text.split()
        
        if not words:
            return [""]
        
        current_line = words[0]
        
        for word in words[1:]:
            test_line = f"{current_line} {word}"
            bbox = draw.textbbox((0, 0), test_line, font=font)
            width = bbox[2] - bbox[0]
            
            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        
        lines.append(current_line)
        return lines
    
    def draw_multiline_text(self, draw: ImageDraw.Draw, position: Tuple[int, int],
                           text: str, font: ImageFont.FreeTypeFont, 
                           fill: Tuple[int, int, int], max_width: int,
                           line_spacing: int = 10, align: str = "left") -> int:
        """
        Draw multiline text with automatic wrapping
        Returns the total height used
        """
        lines = self.wrap_text(text, font, max_width, draw)
        x, y = position
        total_height = 0
        
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            line_height = bbox[3] - bbox[1]
            
            # Calculate x position based on alignment
            if align == "center":
                line_width = bbox[2] - bbox[0]
                text_x = x + (max_width - line_width) // 2
            elif align == "right":
                line_width = bbox[2] - bbox[0]
                text_x = x + max_width - line_width
            else:  # left
                text_x = x
            
            draw.text((text_x, y), line, font=font, fill=fill)
            y += line_height + line_spacing
            total_height += line_height + line_spacing
        
        return total_height - line_spacing  # Remove last line spacing
    
    def draw_text_with_shadow(self, draw: ImageDraw.Draw, position: Tuple[int, int],
                             text: str, font: ImageFont.FreeTypeFont,
                             fill: Tuple[int, int, int], 
                             shadow_color: Tuple[int, int, int] = (0, 0, 0),
                             shadow_offset: Tuple[int, int] = (3, 3)):
        """Draw text with shadow effect"""
        x, y = position
        shadow_x, shadow_y = x + shadow_offset[0], y + shadow_offset[1]
        
        # Draw shadow
        draw.text((shadow_x, shadow_y), text, font=font, fill=shadow_color)
        # Draw text
        draw.text((x, y), text, font=font, fill=fill)
    
    def draw_text_with_outline(self, draw: ImageDraw.Draw, position: Tuple[int, int],
                              text: str, font: ImageFont.FreeTypeFont,
                              fill: Tuple[int, int, int],
                              outline_color: Tuple[int, int, int] = (0, 0, 0),
                              outline_width: int = 2):
        """Draw text with outline effect"""
        x, y = position
        
        # Draw outline
        for adj_x in range(-outline_width, outline_width + 1):
            for adj_y in range(-outline_width, outline_width + 1):
                if adj_x != 0 or adj_y != 0:
                    draw.text((x + adj_x, y + adj_y), text, font=font, fill=outline_color)
        
        # Draw text
        draw.text((x, y), text, font=font, fill=fill)
    
    def get_text_dimensions(self, text: str, font: ImageFont.FreeTypeFont) -> Tuple[int, int]:
        """Get the width and height of text"""
        # Create a dummy image to measure text
        dummy_img = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(dummy_img)
        bbox = draw.textbbox((0, 0), text, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        return width, height
    
    def fit_text_to_width(self, text: str, max_width: int, font_path: str, 
                         max_font_size: int = 100, min_font_size: int = 20) -> ImageFont.FreeTypeFont:
        """Find the largest font size that fits the text within max_width"""
        for size in range(max_font_size, min_font_size - 1, -2):
            font = self.get_font(font_path, size)
            width, _ = self.get_text_dimensions(text, font)
            if width <= max_width:
                return font
        
        # Return minimum size if nothing fits
        return self.get_font(font_path, min_font_size)
