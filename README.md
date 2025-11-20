# 🎨 LinkedIn-Style Post Generator

A powerful, versatile Python library for creating branded social media posts with professional designs, gradients, patterns, and effects.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

### 🎯 Core Capabilities
- **Multiple Post Formats**: Square, vertical, story, horizontal, LinkedIn banner, Twitter post
- **Template System**: 10+ pre-built professional templates
- **12 Color Schemes**: Professional, bold, minimal, gradient, and corporate themes
- **Advanced Typography**: Auto text wrapping, multiple fonts, shadow & outline effects
- **Rich Effects**: Gradients, patterns, vignette, noise, blur

### 🛠️ Tools & Integrations
- **CLI Tool**: Command-line interface for quick generation
- **REST API**: FastAPI-based API for web integration
- **Batch Generator**: Generate hundreds of posts from CSV/JSON
- **Template Loader**: Load, save, and customize templates

### 🎨 Background Styles
- Solid colors
- Linear gradients (vertical, horizontal, diagonal)
- Radial gradients
- Pattern overlays (lines, circles, rectangles, triangles)
- Geometric shapes
- Custom backgrounds

### 📝 Text Features
- Automatic text wrapping
- Multi-line support
- Shadow effects
- Outline effects
- Multiple font styles
- Custom positioning
- Text boxes with backgrounds

## 📦 Installation

```bash
# Clone or download the repository
cd "Post Generator"

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

### Basic Usage

```python
from post_generator import PostGenerator

# Create generator
generator = PostGenerator()

# Create canvas with gradient
generator.create_canvas("square", color=(0, 0, 0))
generator.apply_gradient(
    start_color=(255, 0, 0),
    end_color=(0, 0, 0),
    direction="vertical"
)

# Add text
generator.add_text(
    text="Innovation Starts Here",
    position=(40, 400),
    font_size=70,
    color=(255, 255, 255),
    shadow=True
)

# Save
generator.save("output/my_post.png")
```

### Using Templates

```python
from post_generator import PostGenerator
from post_generator.color_schemes import ColorSchemes
from post_generator.template_loader import TemplateLoader

# Create default templates
loader = TemplateLoader()
loader.create_default_templates()

# Load and use a template
template = loader.load_template("professional_gradient")
color_scheme = ColorSchemes.get_scheme(template.color_scheme)

generator = PostGenerator()
generator.create_canvas(template.dimension, color_scheme.get_background_rgb())
generator.apply_gradient(
    color_scheme.get_primary_rgb(),
    color_scheme.get_secondary_rgb(),
    template.gradient_direction
)
generator.add_text(
    "Your Message Here",
    position=tuple(template.headline_position),
    font_size=template.headline_size,
    color=color_scheme.get_text_rgb(),
    shadow=True
)
generator.save("output/template_post.png")
```

## 🖥️ Command Line Interface

### Generate from Template
```bash
python cli.py --template professional_gradient --text "Innovation starts here" --logo logo.png
```

### Custom Generation
```bash
python cli.py --text "Hello World" --gradient-start "#000000" --gradient-end "#FF0000" --vignette --shadow
```

### List Available Options
```bash
# List templates
python cli.py --list-templates

# List color schemes
python cli.py --list-colors

# Create default templates
python cli.py --create-defaults
```

### CLI Options

| Option | Description |
|--------|-------------|
| `--template, -t` | Template name to use |
| `--text` | Main headline text |
| `--subtext` | Subheadline text |
| `--logo` | Path to logo file |
| `--dimension, -d` | Post dimensions (square, vertical, story, etc.) |
| `--color-scheme, -c` | Color scheme name |
| `--gradient-start` | Gradient start color (hex) |
| `--gradient-end` | Gradient end color (hex) |
| `--pattern` | Pattern type (lines, circles, rectangles) |
| `--vignette` | Add vignette effect |
| `--noise` | Add noise texture |
| `--shadow` | Add text shadow |
| `--outline` | Add text outline |
| `--output, -o` | Output file path |

## 🌐 REST API

### Start the API Server

```bash
python api.py
```

API will be available at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

### API Endpoints

#### Generate Post
```bash
POST /generate
```

**Request Body:**
```json
{
  "text": "Innovation Starts Here",
  "subtext": "Join us today",
  "template": "professional_gradient",
  "dimension": "square",
  "color_scheme": "bold_red",
  "add_vignette": true,
  "text_shadow": true
}
```

**Response:** PNG image file

#### List Templates
```bash
GET /templates
```

#### Get Template Details
```bash
GET /templates/{template_name}
```

#### List Color Schemes
```bash
GET /color-schemes
```

#### Batch Generation
```bash
POST /generate/batch
```

## 📊 Batch Generation

### From CSV

```python
from batch_generator import BatchGenerator

batch = BatchGenerator(output_dir="output/batch")

# Create sample CSV
batch.create_sample_csv("posts.csv")

# Generate from CSV
batch.generate_from_csv("posts.csv", logo_path="logo.png")
```

**CSV Format:**
```csv
template,text,subtext,output_filename
professional_gradient,"Innovation starts here","Join us",post1.png
bold_red_lines,"New Product Launch","Available Now",post2.png
```

### From JSON

```python
batch.generate_from_json("posts.json", logo_path="logo.png")
```

**JSON Format:**
```json
[
  {
    "template": "professional_gradient",
    "text": "Innovation Starts Here",
    "subtext": "Join the future",
    "output_filename": "post1.png"
  }
]
```

### Command Line Batch Generation

```bash
# From CSV
python batch_generator.py --csv posts.csv --logo logo.png --output-dir output/batch

# From JSON
python batch_generator.py --json posts.json --logo logo.png

# Create sample files
python batch_generator.py --create-sample-csv
python batch_generator.py --create-sample-json
```

## 🎨 Available Templates

1. **professional_gradient** - Clean professional look with gradient
2. **bold_red_lines** - Bold red theme with diagonal lines
3. **minimal_clean** - Minimalist gray design
4. **corporate_professional** - Corporate blue with radial gradient
5. **creative_textbox** - Ocean gradient with text boxes
6. **bold_purple_modern** - Modern purple with noise texture
7. **linkedin_story** - Optimized for LinkedIn stories (1080x1920)
8. **sunset_horizontal** - Horizontal format with sunset colors
9. **dark_geometric** - Dark theme with geometric patterns
10. **forest_minimal** - Forest green minimal design

## 🎨 Color Schemes

### Professional
- `professional_dark` - Black and LinkedIn blue
- `professional_blue` - LinkedIn primary colors

### Bold
- `bold_red` - Bold red on black
- `bold_purple` - Vibrant purple
- `bold_orange` - Energetic orange

### Minimal
- `minimal_light` - Clean white and gray
- `minimal_gray` - Subtle gray tones

### Gradient
- `gradient_sunset` - Pink to red sunset
- `gradient_ocean` - Blue to purple ocean
- `gradient_forest` - Green nature gradient

### Corporate
- `corporate_tech` - Tech industry blue
- `corporate_finance` - Finance industry green

## 📐 Dimensions

| Preset | Size | Use Case |
|--------|------|----------|
| `square` | 1080×1080 | LinkedIn, Instagram |
| `square_large` | 1200×1200 | High-res square |
| `vertical` | 1080×1350 | Instagram portrait |
| `story` | 1080×1920 | Instagram/LinkedIn stories |
| `horizontal` | 1200×630 | Facebook, Twitter |
| `linkedin_banner` | 1584×396 | LinkedIn profile banner |
| `twitter_post` | 1200×675 | Twitter posts |

## 🎯 Advanced Features

### Custom Gradients

```python
generator.apply_gradient(
    start_color=(255, 0, 0),
    end_color=(0, 0, 255),
    direction="radial"  # vertical, horizontal, diagonal, radial
)
```

### Pattern Overlays

```python
# Lines
generator.add_pattern_lines(
    color=(255, 255, 255),
    spacing=60,
    angle=45,
    width=3,
    opacity=30
)

# Geometric shapes
generator.add_geometric_shapes(
    shape_type="circles",  # circles, rectangles, triangles
    color=(255, 255, 255),
    opacity=20,
    count=15
)
```

### Effects

```python
# Vignette (darkened edges)
generator.add_vignette(intensity=0.6)

# Noise texture
generator.add_noise(intensity=10)

# Blur
generator.add_blur(radius=5)
```

### Logo Placement

```python
generator.add_logo(
    logo_path="logo.png",
    position="top-left",  # or: top-center, top-right, bottom-left, etc.
    size=(200, 200),
    margin=40
)
```

### Text Boxes

```python
generator.add_text_box(
    text="Important Message",
    box_position=(40, 700),
    box_size=(1000, 200),
    bg_color=(0, 0, 0, 180),  # RGBA
    text_color=(255, 255, 255),
    font_size=50,
    padding=30
)
```

## 📁 Project Structure

```
Post Generator/
├── post_generator/          # Core library
│   ├── __init__.py
│   ├── generator.py         # Main generator class
│   ├── color_schemes.py     # Color scheme definitions
│   ├── typography.py        # Text rendering
│   └── template_loader.py   # Template management
├── templates/               # JSON template files
├── fonts/                   # Custom fonts (add your own)
├── examples/               # Example scripts
│   ├── example_basic.py
│   ├── example_template.py
│   ├── example_advanced.py
│   ├── example_textbox.py
│   ├── example_all_colorschemes.py
│   └── example_batch_csv.py
├── output/                 # Generated images
├── cli.py                  # Command-line tool
├── api.py                  # FastAPI REST API
├── batch_generator.py      # Batch generation utility
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## 🔧 Requirements

- Python 3.7+
- Pillow (PIL)
- FastAPI (for API)
- uvicorn (for API)

## 📖 Examples

Check the `examples/` directory for complete working examples:

- `example_basic.py` - Basic post generation
- `example_template.py` - Using templates
- `example_advanced.py` - Advanced styling features
- `example_textbox.py` - Text boxes with backgrounds
- `example_all_colorschemes.py` - Generate all color schemes
- `example_batch_csv.py` - Batch generation from CSV

Run any example:
```bash
python examples/example_basic.py
```

## 🎓 Tips & Best Practices

1. **Fonts**: Add custom fonts to the `fonts/` directory for better typography
2. **Logos**: Use PNG with transparency for best results
3. **Text Length**: Keep headlines under 50 characters for readability
4. **Colors**: Use high contrast between background and text
5. **Templates**: Customize existing templates instead of starting from scratch
6. **Batch**: Use CSV/JSON for generating multiple variations quickly
7. **API**: Deploy the API to cloud services for team access

## 🤝 Contributing

Feel free to customize templates, add color schemes, or extend functionality!

## 📄 License

MIT License - Feel free to use in personal and commercial projects

## 🆘 Support

For issues or questions:
1. Check the examples directory
2. Review the API documentation at `/docs`
3. Examine template definitions in `templates/`

## 🚀 Next Steps

1. **Add Custom Fonts**: Download fonts and place in `fonts/` directory
2. **Create Templates**: Design templates for your brand
3. **Add Your Logo**: Use your company logo in posts
4. **Batch Generate**: Create multiple posts from CSV data
5. **Deploy API**: Host the API for team access

---

**Built with Python & Pillow** | Made for creating professional social media content at scale
