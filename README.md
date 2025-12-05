# 🎨 Post Generator# 🎨 LinkedIn-Style Post Generator



**Generate stunning social media posts with Python - No design skills needed!**A powerful, versatile Python library for creating branded social media posts with professional designs, gradients, patterns, and effects.



A powerful yet simple tool to create professional social media graphics with:![Version](https://img.shields.io/badge/version-1.0.0-blue)

- 🖼️ **Visual UI** (Streamlit) - Point, click, customize![Python](https://img.shields.io/badge/python-3.7+-green)

- 🔗 **REST API** - Integrate with n8n, Zapier, Make, or any automation tool![License](https://img.shields.io/badge/license-MIT-orange)

- ⚡ **Fast** - Generate images in seconds

- 🎯 **Feature-Rich** - Gradients, patterns, effects, logos, text styling## ✨ Features



---### 🎯 Core Capabilities

- **Multiple Post Formats**: Square, vertical, story, horizontal, LinkedIn banner, Twitter post

## 🚀 Quick Start- **Template System**: 10+ pre-built professional templates

- **12 Color Schemes**: Professional, bold, minimal, gradient, and corporate themes

### 1. Install Dependencies- **Advanced Typography**: Auto text wrapping, multiple fonts, shadow & outline effects

```bash- **Rich Effects**: Gradients, patterns, vignette, noise, blur

pip install -r requirements.txt

```### 🛠️ Tools & Integrations

- **CLI Tool**: Command-line interface for quick generation

### 2. Run Streamlit UI (Visual Interface)- **REST API**: FastAPI-based API for web integration

```bash- **Batch Generator**: Generate hundreds of posts from CSV/JSON

streamlit run streamlit_app.py- **Template Loader**: Load, save, and customize templates

```

Opens at: http://localhost:8501### 🎨 Background Styles

- Solid colors

### 3. Run API Server (For Automation)- Linear gradients (vertical, horizontal, diagonal)

```bash- Radial gradients

python api.py- Pattern overlays (lines, circles, rectangles, triangles)

```- Geometric shapes

Opens at: http://localhost:8000  - Custom backgrounds

API Docs: http://localhost:8000/docs

### 📝 Text Features

---- Automatic text wrapping

- Multi-line support

## 🎯 Features- Shadow effects

- Outline effects

### 🎨 **Canvas & Backgrounds**- Multiple font styles

- **Dimensions:** Square (1080x1080), Story (1080x1920), Horizontal, Wide, Banner, Custom- Custom positioning

- **Backgrounds:** Solid colors, Gradients (5 directions), Color schemes (12 presets)- Text boxes with backgrounds



### 🌈 **Visual Effects**## 📦 Installation

- **Gradients:** Vertical, Horizontal, Diagonal, Radial

- **Patterns:** Lines with custom spacing, angle, width, opacity```bash

- **Shapes:** Circles, Rectangles, Triangles# Clone or download the repository

- **Effects:** Vignette, Noise texture, Blurcd "Post Generator"



### 📝 **Text Styling**# Install dependencies

- **Main Text:** Custom position, size, color, fontpip install -r requirements.txt

- **Effects:** Shadow, Outline```

- **Multi-line:** Automatic line breaks

- **Secondary Text:** Optional tagline/subtext## 🚀 Quick Start

- **Text Boxes:** Colored boxes with custom styling

### Basic Usage

### 🖼️ **Logo Support**

- Upload your logo```python

- 5 positions: Top-left, Top-right, Bottom-left, Bottom-right, Centerfrom post_generator import PostGenerator

- Custom size control

# Create generator

### 🎨 **Color Schemes** (12 Presets)generator = PostGenerator()

- Professional, Bold Purple, Minimal Light, Gradient Sunset

- Corporate Tech, Ocean Breeze, Warm Autumn, Monochrome# Create canvas with gradient

- Vibrant, Pastel Dream, Dark Mode, Nature Greengenerator.create_canvas("square", color=(0, 0, 0))

generator.apply_gradient(

---    start_color=(255, 0, 0),

    end_color=(0, 0, 0),

## 🖥️ Usage    direction="vertical"

)

### Option 1: Visual UI (Streamlit)

# Add text

**Perfect for:** Quick creation, testing, non-technical usersgenerator.add_text(

    text="Innovation Starts Here",

```bash    position=(40, 400),

streamlit run streamlit_app.py    font_size=70,

```    color=(255, 255, 255),

    shadow=True

**Features:**)

- ✅ No coding required

- ✅ Real-time preview# Save

- ✅ Upload logosgenerator.save("output/my_post.png")

- ✅ Download instantly```

- ✅ All features accessible

### Using Templates

**Workflow:**

1. Choose canvas size```python

2. Pick background (color/gradient/scheme)from post_generator import PostGenerator

3. Upload logo (optional)from post_generator.color_schemes import ColorSchemes

4. Add effects (vignette, noise, patterns)from post_generator.template_loader import TemplateLoader

5. Type your text

6. Click "Generate Post"# Create default templates

7. Download!loader = TemplateLoader()

loader.create_default_templates()

---

# Load and use a template

### Option 2: REST API (For Automation)template = loader.load_template("professional_gradient")

color_scheme = ColorSchemes.get_scheme(template.color_scheme)

**Perfect for:** n8n, Zapier, Make, custom integrations, batch processing

generator = PostGenerator()

```bashgenerator.create_canvas(template.dimension, color_scheme.get_background_rgb())

python api.pygenerator.apply_gradient(

```    color_scheme.get_primary_rgb(),

    color_scheme.get_secondary_rgb(),

**Base URL:** `http://localhost:8000`    template.gradient_direction

)

#### 📡 Key Endpointsgenerator.add_text(

    "Your Message Here",

##### 1. Generate Post    position=tuple(template.headline_position),

```http    font_size=template.headline_size,

POST /generate    color=color_scheme.get_text_rgb(),

Content-Type: multipart/form-data    shadow=True

```)

generator.save("output/template_post.png")

**Minimum Example:**```

```json

{## 🖥️ Command Line Interface

  "text": "Hello World"

}### Generate from Template

``````bash

python cli.py --template professional_gradient --text "Innovation starts here" --logo logo.png

**Advanced Example:**```

```json

{### Custom Generation

  "text": "Your Amazing\nHeadline Here",```bash

  "subtext": "Your tagline",python cli.py --text "Hello World" --gradient-start "#000000" --gradient-end "#FF0000" --vignette --shadow

  "dimension": "square",```

  "gradient_start": "#667eea",

  "gradient_end": "#764ba2",### List Available Options

  "add_vignette": true,```bash

  "pattern": "lines",# List templates

  "text_shadow": truepython cli.py --list-templates

}

```# List color schemes

python cli.py --list-colors

##### 2. List Color Schemes

```http# Create default templates

GET /color-schemespython cli.py --create-defaults

``````



##### 3. List Dimensions### CLI Options

```http

GET /dimensions| Option | Description |

```|--------|-------------|

| `--template, -t` | Template name to use |

##### 4. Batch Generate| `--text` | Main headline text |

```http| `--subtext` | Subheadline text |

POST /generate/batch| `--logo` | Path to logo file |

```| `--dimension, -d` | Post dimensions (square, vertical, story, etc.) |

| `--color-scheme, -c` | Color scheme name |

---| `--gradient-start` | Gradient start color (hex) |

| `--gradient-end` | Gradient end color (hex) |

## 🔗 n8n Integration| `--pattern` | Pattern type (lines, circles, rectangles) |

| `--vignette` | Add vignette effect |

### Quick Setup| `--noise` | Add noise texture |

| `--shadow` | Add text shadow |

1. **Start API:** `python api.py`| `--outline` | Add text outline |

2. **In n8n:** Add HTTP Request node| `--output, -o` | Output file path |

   - URL: `http://localhost:8000/generate`

   - Method: POST## 🌐 REST API

   - Body: JSON

### Start the API Server

**Example Workflow:**

```json```bash

{python api.py

  "text": "{{ $json.headline }}",```

  "dimension": "square",

  "color_scheme": "professional",API will be available at `http://localhost:8000`  

  "add_vignette": trueInteractive docs at `http://localhost:8000/docs`

}

```### API Endpoints



See **N8N_INTEGRATION_GUIDE.md** for complete documentation.#### Generate Post

```bash

---POST /generate

```

## 📋 API Parameters (All Optional except text)

**Request Body:**

### Canvas```json

- `dimension`: square, story, vertical, horizontal, wide, banner, custom{

- `custom_width`, `custom_height`: For custom dimensions  "text": "Innovation Starts Here",

  "subtext": "Join us today",

### Background  "template": "professional_gradient",

- `bg_color`: #000000  "dimension": "square",

- `color_scheme`: professional, bold_purple, etc.  "color_scheme": "bold_red",

- `gradient_start`, `gradient_end`: #FF0000  "add_vignette": true,

- `gradient_direction`: vertical, horizontal, diagonal, radial  "text_shadow": true

}

### Patterns & Shapes```

- `pattern`: lines

- `pattern_color`, `pattern_spacing`, `pattern_angle`, `pattern_width`, `pattern_opacity`**Response:** PNG image file

- `shape_type`: circles, rectangles, triangles

- `shape_color`, `shape_count`, `shape_opacity`#### List Templates

```bash

### EffectsGET /templates

- `add_vignette`, `vignette_intensity````

- `add_noise`, `noise_intensity`

- `add_blur`, `blur_radius`#### Get Template Details

```bash

### TextGET /templates/{template_name}

- `text`: Main text (required)```

- `text_x`, `text_y`, `font_size`, `text_color`, `text_max_width`

- `text_shadow`, `text_outline`#### List Color Schemes

- `subtext`, `subtext_x`, `subtext_y`, `subtext_font_size`, `subtext_color````bash

GET /color-schemes

### Text Box```

- `add_textbox`, `textbox_content`

- `textbox_x`, `textbox_y`, `textbox_width`, `textbox_height`#### Batch Generation

- `textbox_bg_color`, `textbox_bg_opacity````bash

- `textbox_text_color`, `textbox_font_size`, `textbox_padding`POST /generate/batch

```

### Logo

- `logo`: File upload## 📊 Batch Generation

- `logo_position`: top-left, top-right, bottom-left, bottom-right, center

- `logo_size`: 50-500### From CSV



---```python

from batch_generator import BatchGenerator

## 📁 Project Structure

batch = BatchGenerator(output_dir="output/batch")

```

Post Generator/# Create sample CSV

├── post_generator/          # Core librarybatch.create_sample_csv("posts.csv")

│   ├── generator.py         # Main generator

│   ├── color_schemes.py     # Color schemes# Generate from CSV

│   ├── typography.py        # Text renderingbatch.generate_from_csv("posts.csv", logo_path="logo.png")

│   └── template_loader.py   # Templates```

├── fonts/                   # Font files

├── output/                  # Generated images**CSV Format:**

├── streamlit_app.py         # Visual UI```csv

├── api.py                   # REST APItemplate,text,subtext,output_filename

├── requirements.txt         # Dependenciesprofessional_gradient,"Innovation starts here","Join us",post1.png

├── README.md               # This filebold_red_lines,"New Product Launch","Available Now",post2.png

└── N8N_INTEGRATION_GUIDE.md # n8n guide```

```

### From JSON

---

```python

## 💡 Quick Examplesbatch.generate_from_json("posts.json", logo_path="logo.png")

```

### Python Code

```python**JSON Format:**

from post_generator import PostGenerator```json

[

gen = PostGenerator()  {

gen.create_canvas("square", (0, 0, 0))    "template": "professional_gradient",

gen.apply_gradient((255, 0, 0), (0, 0, 0), "vertical")    "text": "Innovation Starts Here",

gen.add_text("Hello World", position=(40, 400),     "subtext": "Join the future",

             font_size=70, color=(255, 255, 255), shadow=True)    "output_filename": "post1.png"

gen.save("output/my_post.png")  }

```]

```

### cURL

```bash### Command Line Batch Generation

curl -X POST "http://localhost:8000/generate" \

  -H "Content-Type: application/json" \```bash

  -d '{"text": "Hello World", "gradient_start": "#FF0000", # From CSV

       "gradient_end": "#000000"}' \python batch_generator.py --csv posts.csv --logo logo.png --output-dir output/batch

  --output post.png

```# From JSON

python batch_generator.py --json posts.json --logo logo.png

---

# Create sample files

## 🎯 Tipspython batch_generator.py --create-sample-csv

python batch_generator.py --create-sample-json

1. **Multi-line Text:** Use `\n` or press Enter in Streamlit```

2. **Use Color Schemes:** Easier than manual colors

3. **Stack Effects:** Combine vignette + noise + patterns## 🎨 Available Templates

4. **Logo Positioning:** Test different positions

1. **professional_gradient** - Clean professional look with gradient

---2. **bold_red_lines** - Bold red theme with diagonal lines

3. **minimal_clean** - Minimalist gray design

## 🐛 Troubleshooting4. **corporate_professional** - Corporate blue with radial gradient

5. **creative_textbox** - Ocean gradient with text boxes

**Streamlit won't start:**6. **bold_purple_modern** - Modern purple with noise texture

```bash7. **linkedin_story** - Optimized for LinkedIn stories (1080x1920)

pip install --upgrade streamlit8. **sunset_horizontal** - Horizontal format with sunset colors

```9. **dark_geometric** - Dark theme with geometric patterns

10. **forest_minimal** - Forest green minimal design

**API errors:**

- Check port 8000 is available## 🎨 Color Schemes

- Visit http://localhost:8000/docs for testing

### Professional

**Fonts not loading:**- `professional_dark` - Black and LinkedIn blue

- Fonts in `fonts/` directory will auto-fallback if missing- `professional_blue` - LinkedIn primary colors



---### Bold

- `bold_red` - Bold red on black

## 🚀 Ready to Create!- `bold_purple` - Vibrant purple

- `bold_orange` - Energetic orange

- **Visual UI:** `streamlit run streamlit_app.py`

- **API:** `python api.py`### Minimal

- **Docs:** http://localhost:8000/docs- `minimal_light` - Clean white and gray

- `minimal_gray` - Subtle gray tones

Start generating amazing social media posts! 🚀

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
