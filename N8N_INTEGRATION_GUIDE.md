# 🔗 n8n Integration Guide

Complete guide to integrate Post Generator API with n8n workflows.

## 🚀 Quick Start

### 1. Start the API Server

```bash
cd "E:\Post Generator"
python api.py
```

The API will be available at: `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

---

## 📡 API Endpoints for n8n

### 1. **Health Check**
```
GET http://localhost:8000/health
```
Use this to verify API is running.

---

### 2. **Generate Post (Simple)**
```
POST http://localhost:8000/generate
Content-Type: multipart/form-data
```

**Minimum Required Fields:**
```json
{
  "text": "Your headline here"
}
```

**Response:** PNG image file

---

### 3. **Generate Post (Advanced)**
```
POST http://localhost:8000/generate
Content-Type: multipart/form-data
```

**All Available Options:**

#### Canvas Settings
- `dimension`: "square" | "story" | "vertical" | "horizontal" | "wide" | "banner" | "custom"
- `custom_width`: number (if dimension="custom")
- `custom_height`: number (if dimension="custom")

#### Background
- `bg_color`: "#000000" (hex color)
- `color_scheme`: "professional" | "bold_purple" | "minimal_light" | etc.
- `gradient_start`: "#FF0000" (hex color)
- `gradient_end`: "#000000" (hex color)
- `gradient_direction`: "vertical" | "horizontal" | "diagonal" | "diagonal_reverse" | "radial"

#### Patterns
- `pattern`: "lines"
- `pattern_color`: "#FFFFFF" (hex color)
- `pattern_spacing`: 50 (pixels)
- `pattern_angle`: 45 (degrees)
- `pattern_width`: 2 (pixels)
- `pattern_opacity`: 30 (0-100)

#### Geometric Shapes
- `shape_type`: "circles" | "rectangles" | "triangles"
- `shape_color`: "#FFFFFF" (hex color)
- `shape_count`: 15
- `shape_opacity`: 20 (0-100)

#### Effects
- `add_vignette`: true/false
- `vignette_intensity`: 0.5 (0.0-1.0)
- `add_noise`: true/false
- `noise_intensity`: 5 (1-20)
- `add_blur`: true/false
- `blur_radius`: 5 (1-20)

#### Main Text
- `text`: "Your headline" (required)
- `text_x`: 40 (pixels)
- `text_y`: 400 (pixels)
- `font_size`: 70
- `text_color`: "#FFFFFF" (hex color)
- `text_max_width`: 900 (pixels)
- `text_shadow`: true/false
- `text_outline`: true/false

#### Secondary Text
- `subtext`: "Your tagline"
- `subtext_x`: 40
- `subtext_y`: 650
- `subtext_font_size`: 40
- `subtext_color`: "#AAAAAA" (hex color)

#### Text Box
- `add_textbox`: true/false
- `textbox_content`: "• Line 1\n• Line 2"
- `textbox_x`: 40
- `textbox_y`: 800
- `textbox_width`: 900
- `textbox_height`: 200
- `textbox_bg_color`: "#000000" (hex color)
- `textbox_bg_opacity`: 200 (0-255)
- `textbox_text_color`: "#FFFFFF" (hex color)
- `textbox_font_size`: 35
- `textbox_padding`: 25

#### Logo
- `logo`: Upload file
- `logo_position`: "top-left" | "top-right" | "bottom-left" | "bottom-right" | "center"
- `logo_size`: 150 (pixels)

#### Template Mode
- `template`: "professional_gradient" | "modern_minimal" | etc.

---

### 4. **List Templates**
```
GET http://localhost:8000/templates
```

**Response:**
```json
[
  "professional_gradient",
  "modern_minimal",
  "bold_corporate",
  ...
]
```

---

### 5. **Get Template Details**
```
GET http://localhost:8000/templates/{template_name}
```

**Example:**
```
GET http://localhost:8000/templates/professional_gradient
```

---

### 6. **List Color Schemes**
```
GET http://localhost:8000/color-schemes
```

**Response:**
```json
[
  "professional",
  "bold_purple",
  "minimal_light",
  "gradient_sunset",
  "corporate_tech",
  ...
]
```

---

### 7. **Get Color Scheme Details**
```
GET http://localhost:8000/color-schemes/{scheme_name}
```

**Example:**
```
GET http://localhost:8000/color-schemes/professional
```

**Response:**
```json
{
  "name": "professional",
  "primary": "#2C3E50",
  "secondary": "#34495E",
  "accent": "#3498DB",
  "text": "#FFFFFF",
  "background": "#1A1A1A"
}
```

---

### 8. **List Available Dimensions**
```
GET http://localhost:8000/dimensions
```

**Response:**
```json
{
  "square": {"width": 1080, "height": 1080, "description": "Instagram post"},
  "story": {"width": 1080, "height": 1920, "description": "Instagram/Facebook story"},
  ...
}
```

---

### 9. **Batch Generate**
```
POST http://localhost:8000/generate/batch
Content-Type: application/json
```

**Body:**
```json
[
  {
    "text": "Post 1",
    "dimension": "square",
    "text_color": "#FFFFFF"
  },
  {
    "text": "Post 2",
    "dimension": "story",
    "gradient_start": "#FF0000",
    "gradient_end": "#000000"
  }
]
```

---

## 🛠️ n8n Workflow Examples

### Example 1: Simple Post Generator

**Nodes:**
1. **Webhook** - Receives trigger
2. **HTTP Request** - POST to `/generate`
   - Method: POST
   - URL: `http://localhost:8000/generate`
   - Body: 
     ```json
     {
       "text": "{{ $json.headline }}",
       "subtext": "{{ $json.tagline }}",
       "dimension": "square",
       "gradient_start": "#FF0000",
       "gradient_end": "#000000",
       "text_color": "#FFFFFF"
     }
     ```
3. **Write Binary File** - Save the image

---

### Example 2: Social Media Scheduler

**Nodes:**
1. **Schedule Trigger** - Daily at 9 AM
2. **Google Sheets** - Get content
3. **HTTP Request** - Generate post
   ```json
   {
     "text": "{{ $json.headline }}",
     "dimension": "square",
     "color_scheme": "professional",
     "add_vignette": true,
     "text_shadow": true
   }
   ```
4. **Twitter/Instagram** - Post the image

---

### Example 3: Batch Processing

**Nodes:**
1. **Manual Trigger**
2. **Google Sheets** - Read rows
3. **HTTP Request** - POST to `/generate/batch`
   - Body: Array of all posts
4. **Loop** - Process each result
5. **Save to Cloud Storage**

---

### Example 4: Logo Upload Workflow

**Nodes:**
1. **Webhook** - Receive data
2. **Read Binary File** - Get logo
3. **HTTP Request** - POST to `/generate`
   - Content-Type: multipart/form-data
   - Body:
     - `text`: "{{ $json.text }}"
     - `logo`: Binary file attachment
     - `logo_position`: "top-left"
     - `logo_size`: 150

---

## 💡 Pro Tips

### 1. **Use Color Schemes**
Instead of manually setting colors, use preset schemes:
```json
{
  "text": "My Headline",
  "color_scheme": "professional"
}
```

### 2. **Templates for Consistency**
Use templates for brand consistency:
```json
{
  "text": "My Message",
  "template": "professional_gradient"
}
```

### 3. **Custom Dimensions**
For specific platforms:
```json
{
  "text": "Custom Post",
  "dimension": "custom",
  "custom_width": 1200,
  "custom_height": 628
}
```

### 4. **Multi-line Text**
Use `\n` for line breaks:
```json
{
  "text": "Line 1\nLine 2\nLine 3"
}
```

### 5. **Error Handling**
Always add error handling nodes in n8n:
- Check HTTP status code
- Catch failed requests
- Log errors

---

## 🔐 Security

### For Production:
1. Add authentication to the API
2. Use HTTPS
3. Rate limiting
4. Input validation
5. Store API keys in n8n credentials

---

## 📊 Common Use Cases

### 1. **Quote Posts**
```json
{
  "text": "{{ $json.quote }}",
  "subtext": "- {{ $json.author }}",
  "dimension": "square",
  "gradient_start": "#667eea",
  "gradient_end": "#764ba2",
  "add_vignette": true
}
```

### 2. **Product Announcements**
```json
{
  "text": "{{ $json.product_name }}",
  "subtext": "{{ $json.tagline }}",
  "add_textbox": true,
  "textbox_content": "• {{ $json.feature1 }}\n• {{ $json.feature2 }}\n• {{ $json.feature3 }}",
  "color_scheme": "corporate_tech"
}
```

### 3. **Event Promotion**
```json
{
  "text": "{{ $json.event_name }}",
  "subtext": "{{ $json.date }} | {{ $json.location }}",
  "dimension": "story",
  "pattern": "lines",
  "pattern_angle": 45,
  "add_vignette": true
}
```

---

## 🐛 Troubleshooting

### API Not Responding
```bash
# Check if API is running
curl http://localhost:8000/health
```

### CORS Issues
The API has CORS enabled for all origins. No additional configuration needed.

### Image Not Generating
- Check all required fields are provided
- Verify color hex codes are valid (#RRGGBB)
- Check dimension values are valid
- Review API logs for error messages

---

## 📞 Support

- API Docs: http://localhost:8000/docs
- Interactive testing: Use the `/docs` endpoint
- Test endpoints with Postman/Insomnia before n8n

---

## 🎉 Ready to Go!

Your Post Generator API is fully n8n compatible with:
- ✅ Complete REST API
- ✅ File upload support
- ✅ Batch processing
- ✅ All features exposed
- ✅ CORS enabled
- ✅ Comprehensive endpoints

Start building your automated social media workflows! 🚀
