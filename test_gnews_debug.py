"""Debug script to test GNews article extraction"""

from gnews import GNews
import requests
from newspaper import Article

# Initialize GNews
g = GNews(language='en', country='US', max_results=3)

# Get news articles
print("Fetching news...")
news = g.get_news('artificial intelligence')

for idx, article in enumerate(news, 1):
    print(f"\n{'='*80}")
    print(f"Article {idx}:")
    print(f"  Title: {article.get('title', 'N/A')[:80]}...")
    print(f"  URL: {article.get('url', 'N/A')[:80]}...")
    print(f"  Publisher: {article.get('publisher', {}).get('title', 'N/A')}")
    print(f"  Publisher URL: {article.get('publisher', {}).get('href', 'N/A')}")
    
    # Try to follow the Google News redirect manually
    print(f"\nTrying to resolve Google News URL...")
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(article['url'], allow_redirects=True, timeout=10, headers=headers)
        final_url = response.url
        print(f"  Resolved to: {final_url[:80]}...")
        
        # Now try to extract from the final URL
        if 'news.google.com' not in final_url:
            print(f"  Extracting content from resolved URL...")
            art = Article(final_url)
            art.download()
            art.parse()
            text_len = len(art.text) if art.text else 0
            print(f"  ✓ Success! Text length: {text_len} characters")
            if text_len > 0:
                print(f"  Preview: {art.text[:150]}...")
                break  # Found a working one!
        else:
            print(f"  ✗ Still on Google News - redirect failed")
    except Exception as e:
        print(f"  ✗ Error: {type(e).__name__}: {e}")
