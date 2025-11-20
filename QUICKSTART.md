# 🚀 Quick Start Guide

## Installation

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create default templates**
   ```bash
   python cli.py --create-defaults
   ```

3. **Download fonts (recommended)**
   - Visit [Google Fonts](https://fonts.google.com/)
   - Download: Poppins, Roboto, or Montserrat
   - Place `.ttf` files in the `fonts/` directory

## Generate Your First Post

### Option 1: Using CLI (easiest)

```bash
python cli.py --template professional_gradient --text "Hello World"
```

### Option 2: Using Python Script

Create a file `my_first_post.py`:

```python
from post_generator import PostGenerator

generator = PostGenerator()
generator.create_canvas("square", color=(0, 0, 0))
generator.apply_gradient((255, 0, 0), (0, 0, 0), "vertical")
generator.add_text("Hello World", (40, 400), font_size=70, color=(255, 255, 255))
generator.save("output/hello_world.png")
```

Run it:
```bash
python my_first_post.py
```

### Option 3: Using the API

Start the API:
```bash
python api.py
```

Visit http://localhost:8000/docs and try the interactive API!

## Next Steps

- Explore `examples/` directory
- Read the full [README.md](README.md)
- Try batch generation with CSV files
- Customize templates for your brand

## Common Commands

```bash
# List all templates
python cli.py --list-templates

# List all color schemes
python cli.py --list-colors

# Generate with gradient
python cli.py --text "Your Text" --gradient-start "#000000" --gradient-end "#FF0000"

# Generate with effects
python cli.py --template bold_red_lines --text "Bold Text" --vignette --shadow

# Batch generate from CSV
python batch_generator.py --csv posts.csv
```

## Troubleshooting

**Problem**: "Module not found" error  
**Solution**: Run `pip install -r requirements.txt`

**Problem**: Text looks pixelated  
**Solution**: Add custom fonts to `fonts/` directory

**Problem**: No templates found  
**Solution**: Run `python cli.py --create-defaults`

Happy posting! 🎉
