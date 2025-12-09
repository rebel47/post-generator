# Google News URL Resolution Guide for n8n

## The Problem

Google News RSS URLs (`news.google.com/rss/articles/...`) are redirect/tracking URLs that don't directly resolve to the actual article. Your FastAPI can return these URLs, but scraping them requires special handling in n8n.

## Solution: Two-Step n8n Workflow

### Method 1: Use n8n's Official Template (RECOMMENDED)

1. **Import the official workflow**:
   - Go to: https://n8n.io/workflows/3150-extract-and-decode-google-news-rss-urls-to-clean-article-links/
   - Click "Use Workflow"
   - This template extracts and decodes Google News URLs automatically

2. **Integrate with your FastAPI**:
   ```
   [HTTP Request: Get News] → [n8n Google News Decoder] → [HTTP Request: Scrape Article] → [Your Processing]
   ```

### Method 2: Custom n8n Code Node

Add this Code node between your news fetch and article scrape:

#### Code Node (JavaScript):

```javascript
// Decode Google News URLs to real article URLs
const items = [];

for (const item of $input.all()) {
  const googleUrl = item.json.url;  // Google News URL
  let finalUrl = googleUrl;
  
  // Try to decode the URL
  try {
    // Method 1: Check if URL has embedded link
    const urlMatch = googleUrl.match(/&url=([^&]+)/);
    if (urlMatch) {
      finalUrl = decodeURIComponent(urlMatch[1]);
    }
    // Method 2: Try following the redirect
    else {
      const response = await $http.request({
        url: googleUrl,
        method: 'GET',
        followRedirect: true,
        maxRedirects: 10,
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
      });
      
      // Check if we escaped Google domains
      const redirectedUrl = response.request.href || response.url;
      if (redirectedUrl && !redirectedUrl.includes('google.com')) {
        finalUrl = redirectedUrl;
      }
    }
  } catch (error) {
    console.log(`Could not decode ${googleUrl}: ${error.message}`);
  }
  
  items.push({
    json: {
      ...item.json,
      originalUrl: googleUrl,
      finalUrl: finalUrl,
      wasDecoded: finalUrl !== googleUrl
    }
  });
}

return items;
```

### Method 3: Use the Decode Endpoint

Your FastAPI now has a `/news/decode-google-url` endpoint:

1. **First HTTP Request Node**: Get news
   ```
   GET https://your-ngrok-url.ngrok-free.dev/news/search?keyword=technology
   ```

2. **Second HTTP Request Node**: Decode each URL
   ```
   GET https://your-ngrok-url.ngrok-free.dev/news/decode-google-url?url={{$json["url"]}}
   ```
   This returns:
   ```json
   {
     "recommended_url": "https://actual-article-url.com/...",
     "decoded_url": "...",
     "redirect_url": "..."
   }
   ```

3. **Third HTTP Request Node**: Scrape the decoded URL
   ```
   Use {{$json["recommended_url"]}} for the article content
   ```

## Complete n8n Workflow Example

### Workflow: News → Post Generation

```
1. [Trigger: Schedule] 
   ↓
2. [HTTP Request: Get News]
   GET /news/search?keyword=AI&max_results=5
   ↓
3. [Code: Decode Google URLs]  ← Add the JavaScript code above
   ↓
4. [HTTP Request: Get Article]
   POST /news/article-direct
   URL: {{$json["finalUrl"]}}
   ↓
5. [Code: Format for Post]
   Extract title, summary, format
   ↓
6. [HTTP Request: Generate Post]
   POST /generate/json
   Body: article data
   ↓
7. [Save/Share Post]
```

## Key Points

- **Don't try to scrape Google News URLs directly** - they return Google's wrapper page
- **Decode in n8n** - It's more reliable than server-side decoding
- **The official n8n template** handles most edge cases
- **Fallback**: If decoding fails, use the publisher homepage URL from your API

## Testing

Test the decode endpoint:
```bash
curl "http://localhost:8000/news/decode-google-url?url=https://news.google.com/rss/articles/CBMi..."
```

## Alternative: Use NewsAPI.org Instead

If Google News continues to be problematic, consider switching to NewsAPI.org which provides direct article URLs:
- Free tier: 100 requests/day
- Direct article URLs (no decoding needed)
- Better for automation
