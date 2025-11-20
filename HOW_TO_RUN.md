# 🚀 How to Run Examples

## ✅ All Import Issues Fixed!

All example files now work from any directory.

---

## 📁 Running Examples

### **From Project Root:**

```bash
# Navigate to project root
cd "E:\Post Generator"

# Run any example
python examples\example_custom_design.py
python examples\example_basic.py
python examples\example_template.py
python examples\example_advanced.py
python examples\example_textbox.py
python examples\example_all_colorschemes.py
python examples\example_batch_csv.py

# Run custom design builder
python custom_design_builder.py

# Run demo
python demo.py
```

---

### **From Examples Directory:**

```bash
# Navigate to examples folder
cd "E:\Post Generator\examples"

# Run any example (now works!)
python example_custom_design.py
python example_basic.py
python example_template.py
```

---

## 🎨 Quick Test

Try the custom design examples now:

```bash
cd "E:\Post Generator"
python examples\example_custom_design.py
```

You should see:
```
Creating fully custom design...
   ✓ Saved: output/custom_design_1.png

Creating design with custom brand colors...
   ✓ Saved: output/custom_brand_colors.png

Creating layered effects design...
   ✓ Saved: output/custom_layered.png

... (8 total designs)

✅ All custom designs generated!
```

---

## 📋 All Working Examples

| File | What It Shows | Run Time |
|------|---------------|----------|
| `example_custom_design.py` | 8 completely custom designs | ~5 sec |
| `example_basic.py` | Simple gradient + text | ~1 sec |
| `example_template.py` | Using templates | ~2 sec |
| `example_advanced.py` | Advanced effects & patterns | ~3 sec |
| `example_textbox.py` | Text boxes with backgrounds | ~2 sec |
| `example_all_colorschemes.py` | All 12 color schemes | ~10 sec |
| `example_batch_csv.py` | Batch CSV generation | ~5 sec |

---

## 🎯 Recommended Order

**If you're new:**
1. `example_basic.py` - Start simple
2. `example_template.py` - Learn templates
3. `example_custom_design.py` - See custom designs
4. `demo.py` - See everything

**If you want custom designs:**
1. `example_custom_design.py` - 8 custom examples
2. `custom_design_builder.py` - Easy builder pattern
3. Create your own!

---

## 💡 Create Your Own

After running the examples, create `my_design.py`:

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from post_generator import PostGenerator

gen = PostGenerator()
gen.create_canvas("square", (0, 0, 0))
gen.apply_gradient((255, 0, 0), (0, 0, 255), "diagonal")
gen.add_text("My Design", (40, 400), font_size=80, color=(255, 255, 255))
gen.save("output/my_design.png")
```

Run it:
```bash
python my_design.py
```

---

## ✅ All Fixed!

The import error is resolved. Try running the examples now! 🎨
