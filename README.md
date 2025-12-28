# Post Generator API

A powerful FastAPI-based REST API for generating branded social media posts with advanced customization options, including text styling, gradients, patterns, effects, logo/image overlays, and news integration.

---

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Endpoints](#api-endpoints)
  - [Core Endpoints](#core-endpoints)
  - [Post Generation](#post-generation)
  - [News Integration](#news-integration)
- [Usage Examples](#usage-examples)
- [Streamlit UI](#streamlit-ui)
- [Configuration](#configuration)
- [Development](#development)

---

## ✨ Features

### Post Generation
- **Multiple Canvas Sizes**: Square, vertical, story, horizontal, LinkedIn, Twitter, and custom dimensions
- **Rich Backgrounds**: Solid colors, gradients (vertical, horizontal, diagonal, radial), color schemes
- **Patterns & Shapes**: Line patterns, geometric shapes (circles, triangles, rectangles)
- **Visual Effects**: Vignette, noise texture, blur, shadows, outlines
- **Image Overlays**: Logo and additional image support with position, size, and opacity controls
- **Text Styling**: Multi-line text, custom fonts, colors, shadows, outlines, text boxes
- **Batch Processing**: Generate multiple posts at once
- **Template System**: Pre-defined templates for quick generation

### News Integration
- **Google News RSS**: Fetch trending news by keyword, topic, location, or site
- **URL Decoder**: Decode Google News redirect URLs to actual article URLs
- **Multi-language**: Support for 41 languages and 69 countries
- **Topics**: World, Business, Technology, Entertainment, Sports, Science, Health, Politics, Celebrities

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/rebel47/post-generator.git
cd post-generator
```

2. **Create virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Project structure**
```
Post Generator/
├── api.py                  # Main FastAPI application
├── streamlit_app.py        # Streamlit UI
├── news_fetcher.py         # News fetching module
├── requirements.txt        # Python dependencies
├── post_generator/         # Core generator package
│   ├── generator.py        # Main generator class
│   ├── color_schemes.py    # Color scheme definitions
│   ├── typography.py       # Font handling
│   └── template_loader.py  # Template system
├── fonts/                  # Font files
├── templates/              # JSON template files
└── output/                 # Generated images (auto-created)
```

---

## 🎯 Quick Start

### Start the API Server

```bash
python api.py
```

The API will be available at `http://localhost:8000`

### Access API Documentation

- **Interactive Docs**: http://localhost:8000/docs (Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc (ReDoc)

### Start Streamlit UI

```bash
streamlit run streamlit_app.py
```

The UI will open in your browser at `http://localhost:8501`

---

## 📡 API Endpoints

### Core Endpoints

#### `GET /`
**Root endpoint** - Returns API information and available endpoints

**Response:**
```json
{
  "message": "Post Generator API",
  "version": "1.0.0",
  "endpoints": {
    "/docs": "API documentation",
    "/generate/form": "Generate post (form-data)",
    "/generate/json": "Generate post (JSON)"
  }
}
```

#### `GET /health`
**Health check** - Returns API status

**Response:**
```json
{
  "status": "healthy"
}
```

#### `GET /dimensions`
**Get available dimensions** - Returns list of preset canvas sizes

**Response:**
```json
{
  "dimensions": {
    "square": [1080, 1080],
    "square_large": [1200, 1200],
    "vertical": [1080, 1350],
    "story": [1080, 1920],
    "horizontal": [1200, 630],
    "linkedin_banner": [1584, 396],
    "twitter_post": [1200, 675]
  }
}
```

#### `GET /templates`
**Get available templates** - Returns list of template names

**Response:**
```json
[
  "minimal",
  "bold",
  "gradient",
  "modern",
  "vintage"
]
```

#### `GET /templates/{template_name}`
**Get template details** - Returns specific template configuration

**Response:**
```json
{
  "template_name": "minimal",
  "config": {
    "dimension": "square",
    "gradient_start": "#667eea",
    "gradient_end": "#764ba2"
  }
}
```

#### `GET /color-schemes`
**Get available color schemes** - Returns list of color scheme names

**Response:**
```json
[
  "ocean",
  "sunset",
  "forest",
  "midnight",
  "aurora"
]
```

#### `GET /color-schemes/{scheme_name}`
**Get color scheme details** - Returns specific color scheme configuration

**Response:**
```json
{
  "name": "ocean",
  "primary": "#0066CC",
  "secondary": "#00CCFF",
  "accent": "#FFD700"
}
```

---

### Post Generation

#### `POST /generate/form`
**Generate post with file uploads** - Perfect for n8n and file-based workflows

**Content-Type:** `multipart/form-data`

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | string | *required* | Main text content |
| `subtext` | string | null | Secondary text |
| `dimension` | string | "square" | Canvas size preset or "custom" |
| `custom_width` | int | null | Custom width (if dimension="custom") |
| `custom_height` | int | null | Custom height (if dimension="custom") |

**Background:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `color_scheme` | string | null | Pre-defined color scheme name |
| `bg_color` | string | null | Background color (hex: #RRGGBB) |
| `gradient_start` | string | null | Gradient start color (hex) |
| `gradient_end` | string | null | Gradient end color (hex) |
| `gradient_direction` | string | "vertical" | "vertical", "horizontal", "diagonal", "radial" |

**Patterns:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `pattern` | string | null | Pattern type: "lines" |
| `pattern_color` | string | null | Pattern color (hex) |
| `pattern_angle` | int | 45 | Pattern angle (0-360) |
| `pattern_spacing` | int | 50 | Spacing between pattern elements |
| `pattern_width` | int | 2 | Pattern line width |
| `pattern_opacity` | int | 30 | Pattern opacity (0-100) |

**Shapes:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `shape_type` | string | null | "circle", "triangle", "rectangle" |
| `shape_color` | string | null | Shape color (hex) |
| `shape_count` | int | 15 | Number of shapes |
| `shape_opacity` | int | 20 | Shape opacity (0-100) |

**Effects:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `add_vignette` | bool | false | Add vignette effect |
| `vignette_intensity` | float | 0.5 | Vignette intensity (0.0-1.0) |
| `add_noise` | bool | false | Add noise texture |
| `noise_intensity` | int | 5 | Noise intensity (1-20) |
| `add_blur` | bool | false | Add blur effect |
| `blur_radius` | int | 5 | Blur radius (1-20) |

**Text Styling:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text_x` | int | 40 | Text X position |
| `text_y` | int | 400 | Text Y position |
| `font_size` | int | 70 | Font size |
| `text_color` | string | "#FFFFFF" | Text color (hex) |
| `text_max_width` | int | 900 | Maximum text width |
| `text_shadow` | bool | false | Add text shadow |
| `text_outline` | bool | false | Add text outline |

**Subtext Styling:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `subtext_x` | int | 40 | Subtext X position |
| `subtext_y` | int | 650 | Subtext Y position |
| `subtext_font_size` | int | 40 | Subtext font size |
| `subtext_color` | string | null | Subtext color (hex, defaults to text_color) |

**Logo:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `logo` | file | null | Logo image file (PNG, JPG, JPEG) |
| `logo_position` | string | "top-left" | "top-left", "top-center", "top-right", "bottom-left", "bottom-center", "bottom-right", "center" |
| `logo_size` | int | 150 | Maximum logo dimension |

**Additional Image:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `additional_image` | file | null | Additional image file (PNG, JPG, JPEG) |
| `additional_image_position` | string | "center" | Position (same options as logo) |
| `additional_image_size` | int | null | Maximum image dimension (null = original) |
| `additional_image_opacity` | int | 255 | Image opacity (0-255) |

**Text Box:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `add_textbox` | bool | false | Add text box |
| `textbox_content` | string | null | Text box content |
| `textbox_x` | int | 40 | Text box X position |
| `textbox_y` | int | 800 | Text box Y position |
| `textbox_width` | int | 900 | Text box width |
| `textbox_height` | int | 200 | Text box height |
| `textbox_bg_color` | string | "#000000" | Background color (hex) |
| `textbox_bg_opacity` | int | 200 | Background opacity (0-255) |
| `textbox_text_color` | string | "#FFFFFF" | Text color (hex) |
| `textbox_font_size` | int | 35 | Font size |
| `textbox_padding` | int | 25 | Padding |

**Response:** PNG image file

**Example (curl):**
```bash
curl -X POST "http://localhost:8000/generate/form" \
  -F "text=Hello World" \
  -F "subtext=This is amazing" \
  -F "dimension=square" \
  -F "gradient_start=#667eea" \
  -F "gradient_end=#764ba2" \
  -F "font_size=80" \
  -F "logo=@logo.png" \
  -F "additional_image=@overlay.png" \
  -F "additional_image_opacity=180" \
  -o output.png
```

---

#### `POST /generate/json`
**Generate post from JSON** - No file upload support, perfect for webhooks

**Content-Type:** `application/json`

**Request Body:**
```json
{
  "text": "Your Amazing Headline",
  "subtext": "Subtext or tagline",
  "dimension": "square",
  "gradient_start": "#667eea",
  "gradient_end": "#764ba2",
  "gradient_direction": "vertical",
  "pattern": "lines",
  "pattern_color": "#FFFFFF",
  "pattern_opacity": 20,
  "shape_type": "circle",
  "shape_count": 10,
  "add_vignette": true,
  "text_x": 40,
  "text_y": 400,
  "font_size": 70,
  "text_color": "#FFFFFF",
  "text_shadow": true
}
```

**Response:** PNG image file

---

#### `POST /generate`
**Legacy endpoint** - Simplified post generation (maintained for backward compatibility)

**Request Body:**
```json
{
  "text": "Hello World",
  "dimension": "square",
  "color_scheme": "ocean"
}
```

**Response:** PNG image file

---

#### `POST /generate/batch`
**Generate multiple posts** - Create multiple variations at once

**Request Body:**
```json
{
  "posts": [
    {
      "text": "Post 1",
      "gradient_start": "#667eea",
      "gradient_end": "#764ba2"
    },
    {
      "text": "Post 2",
      "gradient_start": "#f093fb",
      "gradient_end": "#f5576c"
    }
  ]
}
```

**Response:**
```json
{
  "status": "success",
  "count": 2,
  "files": [
    "/tmp/post_uuid1.png",
    "/tmp/post_uuid2.png"
  ]
}
```

---

#### `POST /generate/batch-smart`
**Smart batch generation** - Generate posts with automatic variations

**Request Body:**
```json
{
  "base_post": {
    "dimension": "square",
    "font_size": 70
  },
  "variations": [
    {"text": "Variation 1", "gradient_start": "#667eea"},
    {"text": "Variation 2", "gradient_start": "#f093fb"},
    {"text": "Variation 3", "gradient_start": "#fa709a"}
  ]
}
```

**Response:**
```json
{
  "status": "success",
  "count": 3,
  "files": ["post1.png", "post2.png", "post3.png"]
}
```

---

### News Integration

#### `GET /news/top`
**Get top news headlines**

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `country` | string | "US" | Country code (see /news/available-countries) |
| `language` | string | "en" | Language code (see /news/available-languages) |
| `period` | string | "7d" | Time period: "1h", "24h", "7d", "1m", "1y" |
| `max_results` | int | 10 | Maximum results (1-100) |

**Response:**
```json
{
  "status": "success",
  "count": 10,
  "language": "en",
  "country": "US",
  "period": "7d",
  "articles": [
    {
      "title": "Article Title",
      "description": "Article description",
      "url": "https://news.google.com/rss/articles/...",
      "published date": "Mon, 09 Dec 2024 12:00:00 GMT",
      "publisher": {
        "href": "https://publisher.com",
        "title": "Publisher Name"
      }
    }
  ]
}
```

**Example:**
```bash
curl "http://localhost:8000/news/top?country=US&language=en&max_results=5"
```

---

#### `GET /news/search`
**Search news by keyword**

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `keyword` | string | *required* | Search keyword |
| `country` | string | "US" | Country code |
| `language` | string | "en" | Language code |
| `period` | string | "7d" | Time period |
| `max_results` | int | 10 | Maximum results |

**Response:** Same as `/news/top` with `keyword` field

**Example:**
```bash
curl "http://localhost:8000/news/search?keyword=artificial+intelligence&max_results=5"
```

---

#### `GET /news/topic/{topic}`
**Get news by topic**

**Topics:** `WORLD`, `NATION`, `BUSINESS`, `TECHNOLOGY`, `ENTERTAINMENT`, `SPORTS`, `SCIENCE`, `HEALTH`, `POLITICS`, `CELEBRITIES`

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `country` | string | "US" | Country code |
| `language` | string | "en" | Language code |
| `period` | string | "7d" | Time period |
| `max_results` | int | 10 | Maximum results |

**Response:** Same as `/news/top` with `topic` field

**Example:**
```bash
curl "http://localhost:8000/news/topic/TECHNOLOGY?max_results=5"
```

---

#### `GET /news/location`
**Get news by location**

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `location` | string | *required* | City, state, or country name |
| `country` | string | "US" | Country code |
| `language` | string | "en" | Language code |
| `period` | string | "7d" | Time period |
| `max_results` | int | 10 | Maximum results |

**Example:**
```bash
curl "http://localhost:8000/news/location?location=New+York&max_results=5"
```

---

#### `GET /news/site`
**Get news from specific website**

**Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `site` | string | *required* | Website domain (e.g., "cnn.com") |
| `country` | string | "US" | Country code |
| `language` | string | "en" | Language code |
| `period` | string | "7d" | Time period |
| `max_results` | int | 10 | Maximum results |

**Example:**
```bash
curl "http://localhost:8000/news/site?site=bbc.com&max_results=5"
```

---

#### `GET /news/decode-google-url`
**Decode Google News URL to actual article URL**

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | Google News URL (news.google.com/rss/articles/...) |

**Response:**
```json
{
  "status": "success",
  "original_url": "https://news.google.com/rss/articles/CBMi...",
  "decoded_url": "https://actualwebsite.com/article",
  "message": "URL decoded successfully"
}
```

**Example:**
```bash
curl "http://localhost:8000/news/decode-google-url?url=https://news.google.com/rss/articles/CBMi..."
```

**Use Case in n8n Workflow:**
```
1. GET /news/search → Get news articles
2. GET /news/decode-google-url → Decode article URLs
3. HTTP Request → Scrape article content
4. POST /generate/json → Generate social post
```

---

#### `GET /news/available-countries`
**Get list of supported countries**

**Response:**
```json
{
  "status": "success",
  "count": 69,
  "countries": {
    "US": "United States",
    "GB": "United Kingdom",
    "CA": "Canada",
    "AU": "Australia"
  }
}
```

---

#### `GET /news/available-languages`
**Get list of supported languages**

**Response:**
```json
{
  "status": "success",
  "count": 41,
  "languages": {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German"
  }
}
```

---

#### `GET /news/topics`
**Get list of available news topics**

**Response:**
```json
{
  "status": "success",
  "count": 10,
  "topics": [
    "WORLD",
    "BUSINESS",
    "TECHNOLOGY",
    "ENTERTAINMENT",
    "SPORTS",
    "SCIENCE",
    "HEALTH",
    "POLITICS",
    "CELEBRITIES"
  ]
}
```

---

## 💡 Usage Examples

### Example 1: Simple Post with Gradient

```bash
curl -X POST "http://localhost:8000/generate/json" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Welcome to Our Platform",
    "dimension": "square",
    "gradient_start": "#667eea",
    "gradient_end": "#764ba2",
    "font_size": 80,
    "text_shadow": true
  }' \
  -o welcome_post.png
```

### Example 2: Post with Logo and Pattern

```bash
curl -X POST "http://localhost:8000/generate/form" \
  -F "text=New Product Launch" \
  -F "subtext=Coming Soon" \
  -F "dimension=square" \
  -F "bg_color=#1a1a1a" \
  -F "pattern=lines" \
  -F "pattern_color=#ffffff" \
  -F "pattern_opacity=10" \
  -F "logo=@company_logo.png" \
  -F "logo_position=top-center" \
  -F "text_color=#ffffff" \
  -o product_launch.png
```

### Example 3: News-Driven Post Workflow

```python
import requests

# 1. Fetch news
news_response = requests.get(
    "http://localhost:8000/news/search",
    params={"keyword": "AI", "max_results": 1}
)
article = news_response.json()["articles"][0]

# 2. Decode Google News URL
decode_response = requests.get(
    "http://localhost:8000/news/decode-google-url",
    params={"url": article["url"]}
)
actual_url = decode_response.json()["decoded_url"]

# 3. Generate post
post_response = requests.post(
    "http://localhost:8000/generate/json",
    json={
        "text": article["title"],
        "dimension": "square",
        "gradient_start": "#667eea",
        "gradient_end": "#764ba2",
        "add_textbox": True,
        "textbox_content": actual_url
    }
)

with open("news_post.png", "wb") as f:
    f.write(post_response.content)
```

### Example 4: Batch Generation

```python
import requests

response = requests.post(
    "http://localhost:8000/generate/batch",
    json={
        "posts": [
            {
                "text": "Monday Motivation",
                "gradient_start": "#f093fb",
                "gradient_end": "#f5576c"
            },
            {
                "text": "Tuesday Tips",
                "gradient_start": "#4facfe",
                "gradient_end": "#00f2fe"
            },
            {
                "text": "Wednesday Wisdom",
                "gradient_start": "#43e97b",
                "gradient_end": "#38f9d7"
            }
        ]
    }
)

print(response.json())
```

### Example 5: Using with n8n

**HTTP Request Node Configuration:**

```
Method: POST
URL: http://localhost:8000/generate/form
Body Content Type: Multipart-Form Data

Body Parameters:
- text: {{ $json["title"] }}
- dimension: square
- gradient_start: #667eea
- gradient_end: #764ba2
- font_size: 70
- text_shadow: true

Response Format: File
Binary Property: data
Output File Name: post.png
```

---

## 🎨 Streamlit UI

The project includes a user-friendly Streamlit interface for visual post creation.

### Features:
- **Visual Editor**: Real-time preview of your post
- **File Uploads**: Drag-and-drop logo and additional images
- **Color Pickers**: Visual color selection
- **Sliders**: Easy adjustment of sizes, opacities, and intensities
- **Presets**: Quick access to color schemes and templates
- **Download**: One-click download of generated posts

### Launch:
```bash
streamlit run streamlit_app.py
```

### UI Sections:
1. **Canvas** - Size and dimension selection
2. **Background** - Colors, gradients, schemes
3. **Logo** - Upload and position logo
4. **Additional Image** - Upload overlay images
5. **Effects** - Vignette, noise, blur
6. **Patterns** - Lines and geometric shapes
7. **Text** - Main text styling
8. **Secondary Text** - Optional subtext
9. **Text Box** - Optional text box overlay

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file (optional):

```env
# API Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=False

# File Paths
FONTS_DIR=fonts
TEMPLATES_DIR=templates
OUTPUT_DIR=output

# News API (optional)
NEWS_COUNTRY=US
NEWS_LANGUAGE=en
NEWS_MAX_RESULTS=10
```

### Font Configuration

The API supports custom fonts. Place font files in the `fonts/` directory:

```
fonts/
├── Poppins-Bold.ttf
├── Poppins-Regular.ttf
├── Montserrat-Bold.ttf
└── Roboto-Regular.ttf
```

Default font: `Poppins-Bold.ttf`

### Template System

Create custom templates in `templates/` directory:

**templates/my_template.json:**
```json
{
  "name": "my_template",
  "dimension": "square",
  "gradient_start": "#667eea",
  "gradient_end": "#764ba2",
  "gradient_direction": "diagonal",
  "pattern": "lines",
  "pattern_opacity": 15,
  "font_size": 80,
  "text_shadow": true,
  "add_vignette": true
}
```

---

## 🛠️ Development

### Running with Auto-Reload

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### Running Tests

```bash
# Test news API
python test_news_api.py

# Test URL decoder
python test_decoder.py
```

### Project Structure

```
post_generator/
├── __init__.py
├── generator.py          # Main PostGenerator class
├── color_schemes.py      # Color scheme definitions
├── typography.py         # Font and text handling
└── template_loader.py    # Template system
```

### Adding Custom Color Schemes

Edit `post_generator/color_schemes.py`:

```python
class ColorSchemes:
    @staticmethod
    def get_scheme(name: str) -> ColorScheme:
        schemes = {
            "my_scheme": ColorScheme(
                primary=(102, 126, 234),
                secondary=(118, 75, 162),
                accent=(255, 255, 255),
                background=(26, 26, 26),
                text=(255, 255, 255)
            )
        }
        return schemes.get(name.lower())
```

---

## 📝 API Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid parameters |
| 404 | Not Found - Resource doesn't exist |
| 422 | Validation Error - Invalid data format |
| 500 | Internal Server Error |

---

## 🔒 Security Notes

- **File Uploads**: Validates file types (PNG, JPG, JPEG only)
- **CORS**: Enabled for all origins (configure for production)
- **Temporary Files**: Auto-cleanup after generation
- **Rate Limiting**: Not implemented (add for production)

---

## 📦 Dependencies

**Core:**
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `Pillow` - Image processing
- `pydantic` - Data validation

**News Integration:**
- `gnews` - Google News RSS fetcher
- `newspaper3k` - Article extraction
- `beautifulsoup4` - HTML parsing
- `lxml` - XML/HTML parser

**UI:**
- `streamlit` - Web interface

See `requirements.txt` for full list.

---

## 🚀 Deployment

### Using ngrok (Development)

```bash
# Terminal 1: Start API
python api.py

# Terminal 2: Start ngrok
ngrok http 8000
```

Your API will be available at: `https://your-subdomain.ngrok-free.app`

---

## 🌐 Exposing Endpoints with ngrok

You can use [ngrok](https://ngrok.com/) to make your local API accessible over the internet for testing, webhooks, or integrations (e.g., with n8n, Zapier, or external services).

### Step-by-Step (Windows)

1. **Download ngrok:**
  - Go to https://ngrok.com/download and download the Windows version.
  - Unzip and place `ngrok.exe` in a folder (e.g., `C:\ngrok`).

2. **(Optional) Add ngrok to PATH:**
  - Add the folder containing `ngrok.exe` to your system PATH for easier access from any terminal.

3. **Start your API server:**
  - Open a terminal and run:
    ```bash
    python api.py
    ```

4. **Expose your API with ngrok:**
  - Open a new terminal and run:
    ```bash
    C:\ngrok\ngrok.exe http 8000
    ```
    Or, if added to PATH:
    ```bash
    ngrok http 8000
    ```

5. **Copy the Forwarding URL:**
  - ngrok will display a `Forwarding` URL like `https://your-subdomain.ngrok-free.app`.
  - Use this URL to access your API from anywhere or configure webhooks.

### Example: Test with curl

```bash
curl "https://your-subdomain.ngrok-free.app/health"
```

### Notes
- The free ngrok plan gives you a random subdomain each time you start it.
- For custom subdomains or reserved domains, sign up for a free ngrok account and follow their setup instructions.
- Keep both the API server and ngrok terminal open while testing.

---

### Production Deployment

**Docker:**
```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Docker Compose:**
```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./output:/app/output
    environment:
      - DEBUG=False
```

---

## 🐛 Troubleshooting

### Issue: "Module not found"
```bash
pip install -r requirements.txt
```

### Issue: "Font not found"
Ensure font files are in `fonts/` directory or use absolute paths.

### Issue: "Image not saved"
Check `output/` directory exists and has write permissions:
```bash
mkdir output
chmod 755 output
```

### Issue: "News API not working"
Check internet connection and Google News availability in your region.

### Issue: "Google News URL decoding fails"
Some URLs may be region-locked or expired. Try with fresh news URLs.

---

## 📞 Support

For issues, questions, or contributions:
- **GitHub Issues**: https://github.com/rebel47/post-generator/issues
- **Email**: support@example.com

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Pillow** - Python Imaging Library
- **FastAPI** - Modern web framework
- **GNews** - Google News RSS library
- **Streamlit** - Rapid UI development

---

## 🎉 Quick Reference Card

### Most Common Use Cases

**1. Simple Gradient Post:**
```bash
POST /generate/json
{
  "text": "Hello World",
  "gradient_start": "#667eea",
  "gradient_end": "#764ba2"
}
```

**2. Post with Logo:**
```bash
POST /generate/form
-F "text=Welcome"
-F "logo=@logo.png"
```

**3. News Search:**
```bash
GET /news/search?keyword=AI&max_results=5
```

**4. Decode Google News URL:**
```bash
GET /news/decode-google-url?url=<google_news_url>
```

**5. Batch Posts:**
```bash
POST /generate/batch
{
  "posts": [
    {"text": "Post 1"},
    {"text": "Post 2"}
  ]
}
```

---

**Made with ❤️ by the Post Generator Team**

Happy posting! 🚀
