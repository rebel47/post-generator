"""
Template Loader for Post Generator
Loads and manages post templates from JSON files
"""

import json
import os
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class PostTemplate:
    """Template definition for a post"""
    name: str
    dimension: str
    background_type: str  # "solid", "gradient", "pattern"
    color_scheme: str
    
    # Gradient settings
    gradient_direction: Optional[str] = "vertical"
    
    # Pattern settings
    pattern_type: Optional[str] = None  # "lines", "circles", "rectangles"
    pattern_spacing: Optional[int] = 50
    pattern_angle: Optional[int] = 45
    
    # Effects
    add_vignette: bool = False
    vignette_intensity: float = 0.6
    add_noise: bool = False
    noise_intensity: int = 10
    add_blur_region: bool = False
    
    # Logo settings
    logo_position: str = "top-left"
    logo_size: List[int] = None
    logo_margin: int = 40
    
    # Text settings
    headline_font: str = "fonts/Poppins-Bold.ttf"
    headline_size: int = 70
    headline_position: List[int] = None
    headline_max_width: Optional[int] = 900
    headline_shadow: bool = False
    headline_outline: bool = False
    
    # Subheadline settings
    has_subheadline: bool = False
    subheadline_font: str = "fonts/Poppins-Regular.ttf"
    subheadline_size: int = 40
    subheadline_position: List[int] = None
    subheadline_max_width: Optional[int] = 900
    
    # Text box settings
    use_text_box: bool = False
    text_box_position: List[int] = None
    text_box_size: List[int] = None
    text_box_bg_opacity: int = 180
    
    def __post_init__(self):
        if self.logo_size is None:
            self.logo_size = [200, 200]
        if self.headline_position is None:
            self.headline_position = [40, 400]
        if self.subheadline_position is None:
            self.subheadline_position = [40, 600]
        if self.text_box_position is None:
            self.text_box_position = [40, 700]
        if self.text_box_size is None:
            self.text_box_size = [1000, 200]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert template to dictionary"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PostTemplate':
        """Create template from dictionary"""
        return cls(**data)


class TemplateLoader:
    """Manages loading and saving templates"""
    
    def __init__(self, template_dir: str = "templates"):
        self.template_dir = template_dir
        os.makedirs(template_dir, exist_ok=True)
    
    def load_template(self, name: str) -> PostTemplate:
        """Load a template by name"""
        template_path = os.path.join(self.template_dir, f"{name}.json")
        
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template '{name}' not found at {template_path}")
        
        with open(template_path, 'r') as f:
            data = json.load(f)
        
        return PostTemplate.from_dict(data)
    
    def save_template(self, template: PostTemplate):
        """Save a template to file"""
        template_path = os.path.join(self.template_dir, f"{template.name}.json")
        
        with open(template_path, 'w') as f:
            json.dump(template.to_dict(), f, indent=2)
        
        print(f"✓ Saved template: {template_path}")
    
    def list_templates(self) -> List[str]:
        """List all available templates"""
        if not os.path.exists(self.template_dir):
            return []
        
        templates = []
        for file in os.listdir(self.template_dir):
            if file.endswith('.json'):
                templates.append(file.replace('.json', ''))
        
        return templates
    
    def delete_template(self, name: str):
        """Delete a template"""
        template_path = os.path.join(self.template_dir, f"{name}.json")
        
        if os.path.exists(template_path):
            os.remove(template_path)
            print(f"✓ Deleted template: {name}")
        else:
            print(f"Template '{name}' not found")
    
    def create_default_templates(self):
        """Create a set of default templates"""
        templates = [
            PostTemplate(
                name="professional_gradient",
                dimension="square",
                background_type="gradient",
                color_scheme="professional_dark",
                gradient_direction="vertical",
                add_vignette=True,
                logo_position="top-left",
                headline_position=[40, 400],
                headline_size=70,
                headline_shadow=True
            ),
            PostTemplate(
                name="bold_red_lines",
                dimension="square",
                background_type="gradient",
                color_scheme="bold_red",
                gradient_direction="diagonal",
                pattern_type="lines",
                pattern_angle=45,
                pattern_spacing=60,
                logo_position="top-center",
                headline_position=[40, 500],
                headline_size=80,
                headline_outline=True
            ),
            PostTemplate(
                name="minimal_clean",
                dimension="square",
                background_type="solid",
                color_scheme="minimal_gray",
                logo_position="top-left",
                headline_position=[40, 400],
                headline_size=65,
                has_subheadline=True,
                subheadline_position=[40, 550]
            ),
            PostTemplate(
                name="corporate_professional",
                dimension="square",
                background_type="gradient",
                color_scheme="corporate_tech",
                gradient_direction="radial",
                add_vignette=True,
                vignette_intensity=0.4,
                logo_position="top-right",
                headline_position=[40, 350],
                headline_size=75,
                has_subheadline=True,
                subheadline_position=[40, 520]
            ),
            PostTemplate(
                name="creative_textbox",
                dimension="square",
                background_type="gradient",
                color_scheme="gradient_ocean",
                gradient_direction="diagonal",
                pattern_type="circles",
                use_text_box=True,
                text_box_position=[40, 650],
                text_box_size=[1000, 300],
                logo_position="top-left",
                headline_position=[40, 350],
                headline_size=70
            ),
            PostTemplate(
                name="bold_purple_modern",
                dimension="square",
                background_type="gradient",
                color_scheme="bold_purple",
                gradient_direction="vertical",
                add_noise=True,
                noise_intensity=5,
                logo_position="top-center",
                headline_position=[40, 450],
                headline_size=80,
                headline_shadow=True
            ),
            PostTemplate(
                name="linkedin_story",
                dimension="story",
                background_type="gradient",
                color_scheme="professional_blue",
                gradient_direction="vertical",
                add_vignette=True,
                logo_position="top-center",
                logo_size=[250, 250],
                logo_margin=60,
                headline_position=[60, 600],
                headline_size=90,
                headline_max_width=960
            ),
            PostTemplate(
                name="sunset_horizontal",
                dimension="horizontal",
                background_type="gradient",
                color_scheme="gradient_sunset",
                gradient_direction="horizontal",
                pattern_type="lines",
                pattern_angle=135,
                logo_position="center",
                headline_position=[50, 250],
                headline_size=85,
                headline_max_width=1100
            ),
            PostTemplate(
                name="dark_geometric",
                dimension="square",
                background_type="gradient",
                color_scheme="professional_dark",
                gradient_direction="radial",
                pattern_type="rectangles",
                add_vignette=True,
                logo_position="top-left",
                headline_position=[40, 400],
                headline_size=70,
                headline_outline=True
            ),
            PostTemplate(
                name="forest_minimal",
                dimension="square",
                background_type="gradient",
                color_scheme="gradient_forest",
                gradient_direction="vertical",
                add_noise=True,
                noise_intensity=8,
                logo_position="top-right",
                headline_position=[40, 420],
                headline_size=68,
                has_subheadline=True,
                subheadline_position=[40, 580]
            )
        ]
        
        for template in templates:
            self.save_template(template)
        
        print(f"✓ Created {len(templates)} default templates")
