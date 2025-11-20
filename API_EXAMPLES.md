# API Usage Examples

## Starting the API

```bash
python api.py
```

The API will be available at:
- Base URL: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- OpenAPI Schema: http://localhost:8000/openapi.json

## cURL Examples

### 1. List Templates

```bash
curl http://localhost:8000/templates
```

### 2. Get Template Details

```bash
curl http://localhost:8000/templates/professional_gradient
```

### 3. List Color Schemes

```bash
curl http://localhost:8000/color-schemes
```

### 4. Generate Simple Post

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Innovation Starts Here",
    "template": "professional_gradient",
    "dimension": "square"
  }' \
  --output post.png
```

### 5. Generate with Custom Gradient

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Custom Design",
    "gradient_start": "#FF0000",
    "gradient_end": "#000000",
    "gradient_direction": "diagonal",
    "dimension": "square",
    "add_vignette": true,
    "text_shadow": true
  }' \
  --output custom_post.png
```

### 6. Generate with Logo Upload

```bash
curl -X POST "http://localhost:8000/generate" \
  -F "logo=@path/to/logo.png" \
  -F 'request={
    "text": "Company Post",
    "template": "professional_gradient",
    "logo_position": "top-left"
  }' \
  --output branded_post.png
```

## Python Requests Examples

```python
import requests

# 1. Simple generation
response = requests.post(
    "http://localhost:8000/generate",
    json={
        "text": "Hello World",
        "template": "bold_red_lines",
        "dimension": "square"
    }
)

with open("output.png", "wb") as f:
    f.write(response.content)

# 2. With logo upload
files = {"logo": open("logo.png", "rb")}
data = {
    "request": json.dumps({
        "text": "Branded Post",
        "template": "professional_gradient"
    })
}

response = requests.post(
    "http://localhost:8000/generate",
    files=files,
    data=data
)

with open("branded.png", "wb") as f:
    f.write(response.content)

# 3. List templates
templates = requests.get("http://localhost:8000/templates").json()
print(templates)

# 4. Get color scheme
scheme = requests.get("http://localhost:8000/color-schemes/bold_red").json()
print(scheme)
```

## JavaScript/Node.js Examples

```javascript
// Using fetch
async function generatePost() {
  const response = await fetch('http://localhost:8000/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: 'JavaScript Post',
      template: 'minimal_clean',
      dimension: 'square'
    })
  });
  
  const blob = await response.blob();
  // Save or display the image
}

// Using axios
const axios = require('axios');
const fs = require('fs');

async function generatePost() {
  const response = await axios.post(
    'http://localhost:8000/generate',
    {
      text: 'Node.js Post',
      template: 'corporate_professional',
      add_vignette: true
    },
    { responseType: 'arraybuffer' }
  );
  
  fs.writeFileSync('post.png', response.data);
}
```

## Response Codes

- `200 OK` - Post generated successfully
- `404 Not Found` - Template or color scheme not found
- `422 Unprocessable Entity` - Invalid request parameters
- `500 Internal Server Error` - Generation error

## Request Parameters

### PostRequest Model

```json
{
  "text": "string (required)",
  "subtext": "string (optional)",
  "template": "string (optional)",
  "dimension": "string (default: square)",
  "color_scheme": "string (optional)",
  "gradient_start": "string (hex color, optional)",
  "gradient_end": "string (hex color, optional)",
  "gradient_direction": "string (default: vertical)",
  "pattern": "string (optional: lines, circles, rectangles)",
  "pattern_angle": "integer (default: 45)",
  "pattern_spacing": "integer (default: 50)",
  "add_vignette": "boolean (default: false)",
  "add_noise": "boolean (default: false)",
  "text_shadow": "boolean (default: false)",
  "text_outline": "boolean (default: false)",
  "font_size": "integer (default: 70)",
  "text_color": "string (hex color, default: #FFFFFF)",
  "logo_position": "string (default: top-left)"
}
```

## Production Deployment

### Using Gunicorn (Linux/Mac)

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker api:app
```

### Using Docker

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t post-generator-api .
docker run -p 8000:8000 post-generator-api
```

### Environment Variables

```bash
export API_HOST=0.0.0.0
export API_PORT=8000
export MAX_FILE_SIZE_MB=10
export ENABLE_CORS=true
```
