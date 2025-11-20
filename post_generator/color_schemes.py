"""
Color Scheme Manager for Post Generator
Provides preset color themes and custom color support
"""

from typing import Tuple, List, Dict
from dataclasses import dataclass


@dataclass
class ColorScheme:
    """Color scheme definition for posts"""
    name: str
    primary: str
    secondary: str
    accent: str
    text: str
    background: str
    
    def to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def get_primary_rgb(self) -> Tuple[int, int, int]:
        return self.to_rgb(self.primary)
    
    def get_secondary_rgb(self) -> Tuple[int, int, int]:
        return self.to_rgb(self.secondary)
    
    def get_accent_rgb(self) -> Tuple[int, int, int]:
        return self.to_rgb(self.accent)
    
    def get_text_rgb(self) -> Tuple[int, int, int]:
        return self.to_rgb(self.text)
    
    def get_background_rgb(self) -> Tuple[int, int, int]:
        return self.to_rgb(self.background)


class ColorSchemes:
    """Predefined color schemes"""
    
    # Professional themes
    PROFESSIONAL_DARK = ColorScheme(
        name="professional_dark",
        primary="#000000",
        secondary="#1a1a1a",
        accent="#0077B5",  # LinkedIn blue
        text="#FFFFFF",
        background="#000000"
    )
    
    PROFESSIONAL_BLUE = ColorScheme(
        name="professional_blue",
        primary="#0A66C2",  # LinkedIn primary
        secondary="#004182",
        accent="#70B5F9",
        text="#FFFFFF",
        background="#0A66C2"
    )
    
    # Bold themes
    BOLD_RED = ColorScheme(
        name="bold_red",
        primary="#FF0000",
        secondary="#CC0000",
        accent="#FF6B6B",
        text="#FFFFFF",
        background="#000000"
    )
    
    BOLD_PURPLE = ColorScheme(
        name="bold_purple",
        primary="#8B00FF",
        secondary="#6200CC",
        accent="#B47AEA",
        text="#FFFFFF",
        background="#1a0033"
    )
    
    BOLD_ORANGE = ColorScheme(
        name="bold_orange",
        primary="#FF6B00",
        secondary="#CC5500",
        accent="#FFA500",
        text="#FFFFFF",
        background="#1a0f00"
    )
    
    # Minimal themes
    MINIMAL_LIGHT = ColorScheme(
        name="minimal_light",
        primary="#FFFFFF",
        secondary="#F5F5F5",
        accent="#333333",
        text="#000000",
        background="#FFFFFF"
    )
    
    MINIMAL_GRAY = ColorScheme(
        name="minimal_gray",
        primary="#2C3E50",
        secondary="#34495E",
        accent="#95A5A6",
        text="#ECF0F1",
        background="#2C3E50"
    )
    
    # Gradient themes
    GRADIENT_SUNSET = ColorScheme(
        name="gradient_sunset",
        primary="#FF416C",
        secondary="#FF4B2B",
        accent="#FFD700",
        text="#FFFFFF",
        background="#1a0000"
    )
    
    GRADIENT_OCEAN = ColorScheme(
        name="gradient_ocean",
        primary="#667EEA",
        secondary="#764BA2",
        accent="#A8DADC",
        text="#FFFFFF",
        background="#1a1a2e"
    )
    
    GRADIENT_FOREST = ColorScheme(
        name="gradient_forest",
        primary="#11998E",
        secondary="#38EF7D",
        accent="#CCFF00",
        text="#FFFFFF",
        background="#0d2818"
    )
    
    # Corporate themes
    CORPORATE_TECH = ColorScheme(
        name="corporate_tech",
        primary="#1E3A8A",
        secondary="#3B82F6",
        accent="#60A5FA",
        text="#FFFFFF",
        background="#0F172A"
    )
    
    CORPORATE_FINANCE = ColorScheme(
        name="corporate_finance",
        primary="#064E3B",
        secondary="#10B981",
        accent="#34D399",
        text="#FFFFFF",
        background="#022C22"
    )
    
    @classmethod
    def get_all_schemes(cls) -> Dict[str, ColorScheme]:
        """Get all available color schemes"""
        return {
            "professional_dark": cls.PROFESSIONAL_DARK,
            "professional_blue": cls.PROFESSIONAL_BLUE,
            "bold_red": cls.BOLD_RED,
            "bold_purple": cls.BOLD_PURPLE,
            "bold_orange": cls.BOLD_ORANGE,
            "minimal_light": cls.MINIMAL_LIGHT,
            "minimal_gray": cls.MINIMAL_GRAY,
            "gradient_sunset": cls.GRADIENT_SUNSET,
            "gradient_ocean": cls.GRADIENT_OCEAN,
            "gradient_forest": cls.GRADIENT_FOREST,
            "corporate_tech": cls.CORPORATE_TECH,
            "corporate_finance": cls.CORPORATE_FINANCE,
        }
    
    @classmethod
    def get_scheme(cls, name: str) -> ColorScheme:
        """Get a color scheme by name"""
        schemes = cls.get_all_schemes()
        if name not in schemes:
            raise ValueError(f"Color scheme '{name}' not found. Available: {list(schemes.keys())}")
        return schemes[name]
    
    @classmethod
    def list_schemes(cls) -> List[str]:
        """List all available scheme names"""
        return list(cls.get_all_schemes().keys())
