"""
LinkedIn-style Post Generator
A versatile image generation library for creating branded social media posts
"""

from .generator import PostGenerator
from .color_schemes import ColorScheme
from .typography import Typography
from .template_loader import TemplateLoader

__version__ = "1.0.0"
__all__ = ["PostGenerator", "ColorScheme", "Typography", "TemplateLoader"]
