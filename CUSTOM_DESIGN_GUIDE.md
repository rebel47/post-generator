# 🎨 Custom Design Guide

## Yes! You Can Do **Completely Custom Designs**

The Post Generator gives you **100% control** over every element. No templates required!

---

## 🚀 Quick Custom Design Examples

### 1. **Simple Custom Design**

```python
from post_generator import PostGenerator

gen = PostGenerator()

# Your exact specifications
gen.create_canvas((1200, 1200), color=(20, 20, 40))
gen.apply_gradient((138, 43, 226), (255, 20, 147), "diagonal")
gen.add_pattern_lines((255, 255, 255), spacing=60, angle=45, opacity=25)
gen.add_vignette(0.6)
gen.add_text("YOUR DESIGN", (40, 400), font_size=90, color=(255, 255, 255))
gen.save("output/my_design.png")
```

### 2. **Using Hex Colors**

```python
# Define your brand colors
BRAND_PRIMARY = "#0066CC"
BRAND_SECONDARY = "#FF6600"

# Convert hex to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

primary = hex_to_rgb(BRAND_PRIMARY)
secondary = hex_to_rgb(BRAND_SECONDARY)

gen = PostGenerator()
gen.create_canvas("square", primary)
gen.apply_gradient(primary, secondary, "vertical")
gen.add_text("Brand Colors", (40, 400), font_size=80, color=(255, 255, 255))
gen.save("output/brand_design.png")
```

### 3. **Fluent API Builder** (Easiest!)

```python
from custom_design_builder import CustomDesignBuilder

design = CustomDesignBuilder()

design \
    .set_dimension('square') \
    .set_background('#000000') \
    .add_gradient('#8B00FF', '#FF1493', 'diagonal') \
    .add_pattern_lines('#FFFFFF', spacing=60, angle=45) \
    .add_shapes('circles', '#FFD700', opacity=20, count=15) \
    .add_vignette(0.6) \
    .add_text('CUSTOM', 40, 400, font_size=90, color='#FFFFFF', shadow=True) \
    .build('output/my_design.png')
```

---

## 🎨 What You Can Customize

### ✅ **Dimensions**
```python
# Preset dimensions
gen.create_canvas("square", color)      # 1080x1080
gen.create_canvas("vertical", color)    # 1080x1350
gen.create_canvas("story", color)       # 1080x1920

# ANY custom size
gen.create_canvas((1500, 800), color)   # Custom width x height
gen.create_canvas((2000, 2000), color)  # Ultra high-res
```

### ✅ **Colors**
```python
# RGB tuples
color = (255, 0, 0)  # Red

# Hex colors (with builder)
color = "#FF0000"

# Any color imaginable
custom_purple = (138, 43, 226)
brand_blue = (0, 102, 204)
```

### ✅ **Gradients**
```python
# 4 directions + radial
gen.apply_gradient(start, end, "vertical")
gen.apply_gradient(start, end, "horizontal")
gen.apply_gradient(start, end, "diagonal")
gen.apply_gradient(start, end, "radial")

# Any colors you want
gen.apply_gradient((255, 0, 0), (0, 0, 255), "diagonal")
```

### ✅ **Patterns**
```python
# Lines - any angle, any spacing
gen.add_pattern_lines(
    color=(255, 255, 255),
    spacing=50,    # Distance between lines
    angle=45,      # 0-360 degrees
    width=2,       # Line thickness
    opacity=30     # Transparency
)

# Geometric shapes
gen.add_geometric_shapes(
    shape_type="circles",      # circles, rectangles, triangles
    color=(255, 255, 255),
    opacity=20,
    count=15                   # Number of shapes
)

# Layer multiple patterns!
gen.add_pattern_lines(...) # First layer
gen.add_pattern_lines(...) # Second layer
gen.add_geometric_shapes(...) # Third layer
```

### ✅ **Effects**
```python
# Vignette (darkened edges)
gen.add_vignette(intensity=0.6)  # 0.0 to 1.0

# Noise texture
gen.add_noise(intensity=10)  # 0 to 50

# Blur
gen.add_blur(radius=5)  # Any radius

# Blur specific region only
gen.add_blur(radius=5, region=(x1, y1, x2, y2))
```

### ✅ **Text**
```python
# Complete control
gen.add_text(
    text="Your Text",
    position=(40, 400),          # Exact position
    font_size=70,                # Any size
    color=(255, 255, 255),       # Any color
    max_width=900,               # Auto wrap
    shadow=True,                 # Drop shadow
    outline=True,                # Text outline
    font_path="fonts/Custom.ttf" # Custom font
)

# Text boxes
gen.add_text_box(
    text="Box Content",
    box_position=(40, 700),
    box_size=(1000, 200),
    bg_color=(0, 0, 0, 180),     # RGBA - transparent!
    text_color=(255, 255, 255),
    font_size=40,
    padding=30
)

# Multiple text elements
gen.add_text("Title", (40, 300), font_size=90)
gen.add_text("Subtitle", (40, 450), font_size=50)
gen.add_text("Footer", (40, 900), font_size=30)
```

### ✅ **Logo**
```python
# 9 preset positions
gen.add_logo("logo.png", position="top-left")
gen.add_logo("logo.png", position="top-center")
gen.add_logo("logo.png", position="center")

# Custom position
gen.add_logo("logo.png", custom_position=(100, 100))

# Custom size
gen.add_logo("logo.png", size=(300, 300))
```

---

## 🎨 Design Styles You Can Create

### **1. Corporate Professional**
```python
gen.create_canvas("square", (10, 30, 70))
gen.apply_gradient((10, 30, 70), (20, 60, 140), "vertical")
gen.add_vignette(0.4)
gen.add_text("Corporate", (40, 400), font_size=80, color=(255, 255, 255))
```

### **2. Bold & Vibrant**
```python
gen.create_canvas("square", (0, 0, 0))
gen.apply_gradient((255, 0, 100), (255, 200, 0), "diagonal")
gen.add_pattern_lines((255, 255, 255), spacing=50, angle=45, opacity=30)
gen.add_text("BOLD", (40, 400), font_size=100, color=(255, 255, 255), outline=True)
```

### **3. Minimalist Clean**
```python
gen.create_canvas("square", (250, 250, 250))
gen.add_text("MINIMAL", (40, 40), font_size=50, color=(50, 50, 50))
gen.add_text("Less is More", (40, 450), font_size=80, color=(30, 30, 30))
```

### **4. Neon Cyberpunk**
```python
gen.create_canvas("square", (10, 0, 20))
gen.apply_gradient((10, 0, 20), (50, 0, 80), "vertical")
gen.add_pattern_lines((255, 0, 255), spacing=60, angle=0, opacity=40)
gen.add_pattern_lines((0, 255, 255), spacing=60, angle=90, opacity=40)
gen.add_vignette(0.8)
gen.add_text("NEON", (40, 400), font_size=120, color=(255, 0, 255), outline=True)
```

### **5. Abstract Art**
```python
gen.create_canvas("square", (20, 20, 20))
gen.apply_gradient((255, 50, 50), (50, 50, 255), "diagonal")
gen.add_geometric_shapes("circles", (255, 255, 0), opacity=30, count=20)
gen.add_geometric_shapes("rectangles", (0, 255, 255), opacity=25, count=15)
gen.add_vignette(0.7)
```

### **6. Data Visualization**
```python
gen.create_canvas("horizontal", (5, 15, 35))
gen.apply_gradient((5, 15, 35), (10, 40, 80), "horizontal")
gen.add_pattern_lines((0, 150, 255), spacing=100, angle=0, opacity=20)
gen.add_pattern_lines((0, 150, 255), spacing=100, angle=90, opacity=20)
gen.add_text("DATA DRIVEN", (50, 250), font_size=75, color=(0, 255, 255))
```

### **7. Magazine Cover**
```python
gen.create_canvas("vertical", (255, 255, 255))
gen.apply_gradient((220, 20, 60), (139, 0, 0), "diagonal")
gen.add_text_box("MAGAZINE", (0, 0), (1080, 180), 
                 bg_color=(0, 0, 0, 255), font_size=42)
gen.add_text("BIG HEADLINE", (60, 400), font_size=95, 
             color=(255, 255, 255), shadow=True)
```

### **8. Tech/Grid Style**
```python
gen.create_canvas("square", (10, 20, 40))
# Create grid by layering lines
for i in range(0, 1080, 100):
    gen.add_pattern_lines((0, 150, 255), spacing=1080, angle=90, opacity=30)
gen.add_pattern_lines((0, 150, 255), spacing=100, angle=0, opacity=20)
```

---

## 📋 Full Custom Design Workflow

### **Step 1: Plan Your Design**
- Decide on dimensions
- Choose your colors
- Plan text placement
- Consider effects

### **Step 2: Create Canvas**
```python
from post_generator import PostGenerator

gen = PostGenerator()
gen.create_canvas((width, height), background_color)
```

### **Step 3: Add Background**
```python
# Option A: Solid color (already set in canvas)

# Option B: Gradient
gen.apply_gradient(start_color, end_color, direction)
```

### **Step 4: Add Patterns (Optional)**
```python
gen.add_pattern_lines(color, spacing, angle, width, opacity)
gen.add_geometric_shapes(shape_type, color, opacity, count)
```

### **Step 5: Add Effects (Optional)**
```python
gen.add_vignette(intensity)
gen.add_noise(intensity)
gen.add_blur(radius)
```

### **Step 6: Add Content**
```python
# Add logo
gen.add_logo("logo.png", position="top-left")

# Add text
gen.add_text("Headline", (x, y), font_size=80, color=(255, 255, 255))
gen.add_text("Subtext", (x, y), font_size=40, color=(200, 200, 200))

# Add text boxes
gen.add_text_box("Content", (x, y), (width, height), ...)
```

### **Step 7: Save**
```python
gen.save("output/my_custom_design.png")
```

---

## 🔥 Advanced Techniques

### **Layering Multiple Effects**
```python
# Stack effects for unique looks
gen.apply_gradient(color1, color2, "radial")
gen.add_pattern_lines(color3, 50, 45, 2, 20)
gen.add_pattern_lines(color4, 50, 135, 2, 20)  # Cross pattern
gen.add_geometric_shapes("circles", color5, 15, 10)
gen.add_vignette(0.6)
gen.add_noise(5)
```

### **Complex Text Layouts**
```python
# Header
gen.add_text_box("HEADER", (0, 0), (1080, 150), ...)

# Main content
gen.add_text("Title", (40, 300), font_size=90, ...)
gen.add_text("Subtitle", (40, 450), font_size=50, ...)

# Stats box
gen.add_text_box("Stats:\nMetric 1\nMetric 2", (40, 650), (500, 300), ...)

# Footer
gen.add_text("Footer text", (40, 1000), font_size=30, ...)
```

### **Creating Patterns**
```python
# Grid pattern
gen.add_pattern_lines(color, 100, 0, 1, 20)   # Horizontal
gen.add_pattern_lines(color, 100, 90, 1, 20)  # Vertical

# Diagonal cross
gen.add_pattern_lines(color, 80, 45, 2, 25)
gen.add_pattern_lines(color, 80, 135, 2, 25)

# Radial-like pattern with shapes
gen.add_geometric_shapes("circles", color, 15, 30)
```

---

## 🎓 Examples to Run

### **Try the Custom Examples:**
```bash
# 8 completely custom designs
python examples/example_custom_design.py

# Builder pattern examples
python custom_design_builder.py
```

### **Or Create Your Own:**
```bash
# Create a new file: my_design.py

from post_generator import PostGenerator

gen = PostGenerator()
gen.create_canvas("square", (YOUR_COLOR))
gen.apply_gradient((COLOR1), (COLOR2), "diagonal")
# ... add your customizations ...
gen.save("output/my_design.png")

# Run it
python my_design.py
```

---

## 💡 Pro Tips

1. **Start Simple** - Add one element at a time
2. **Test Colors** - Use small sizes first to test quickly
3. **Layer Carefully** - Order matters (background → patterns → effects → content)
4. **Use Opacity** - Makes overlays blend nicely
5. **Save Versions** - Save multiple versions as you build
6. **Reference Designs** - Look at designs you like and recreate them

---

## 🎨 Color Resources

### **Get Color Inspiration:**
- [Coolors.co](https://coolors.co/) - Color palette generator
- [Adobe Color](https://color.adobe.com/) - Color wheel
- [Color Hunt](https://colorhunt.co/) - Trending palettes

### **Convert Hex to RGB:**
```python
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Use it
my_color = hex_to_rgb("#FF6B6B")
```

---

## 📚 More Examples

Check these files:
- `examples/example_custom_design.py` - 8 custom designs
- `custom_design_builder.py` - Builder pattern
- `examples/example_advanced.py` - Advanced effects
- `demo.py` - Various styles

---

## ✅ Summary

**YES** - You can create **ANY custom design** you want!

✅ Any dimensions
✅ Any colors  
✅ Any gradients
✅ Any patterns
✅ Any effects
✅ Any text styling
✅ Complete control

**No templates required!**

Start creating: `python examples/example_custom_design.py`
