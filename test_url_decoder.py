"""Test Google News URL decoder"""

from news_fetcher import decode_google_news_url
import base64
import re

# Test with actual Google News URLs
test_urls = [
    "https://news.google.com/rss/articles/CBMigwJBVV95cUxPY1QxRG0wYTNXOXg3eFdRd3dUbWtYLXFiUm5CMV9ZeWo3OWVlaDQ4dHNQclVYQmdocHBZYU9KbVp2TVVLMDJwWEUzQlBzVGdYd0xpcDR1TFFFNzJzS1FWUUs3SExqei11YV94czRMNE1YVGRtMGNvdWlmd1ZYWlB3WFBwTUJiUTluOHFIN1h2U0dmWnZjMUxJNzlLZTd2dERJcHBfWDVsc2lnVjhaQnVMWnhDWXdOV0FwVHVQRktTNHdkV2RSbFp5UXE3UWY4eWZTQ1dhRjNuMmNibWxHdTVyOEVfU29UUDVUYlZFNC10c3NMbk8zZzBfaWFfZUcxeDRNZ3U4?oc=5&hl=en-US&gl=US&ceid=US:en",
]

print("Testing Google News URL Decoder\n" + "="*80)

for idx, url in enumerate(test_urls, 1):
    print(f"\nTest {idx}:")
    print(f"  Original: {url[:80]}...")
    
    # Extract the article ID
    match = re.search(r'/articles/([A-Za-z0-9_-]+)', url)
    if match:
        article_id = match.group(1)
        print(f"  Article ID: {article_id[:50]}...")
        
        # Try different decoding methods
        try:
            # Method 1: Direct base64
            decoded_bytes = base64.b64decode(article_id + '==')
            decoded_text = decoded_bytes.decode('utf-8', errors='ignore')
            print(f"  Decoded (base64): {decoded_text[:200]}")
            
            # Look for URLs
            urls_found = re.findall(r'https?://[^\s<>"]+', decoded_text)
            if urls_found:
                print(f"  ✓ Found URLs: {urls_found}")
        except Exception as e:
            print(f"  Base64 decode failed: {e}")
        
        # Method 2: URL-safe base64
        try:
            # Replace URL-safe chars
            b64_std = article_id.replace('-', '+').replace('_', '/')
            # Add padding
            padding = 4 - (len(b64_std) % 4)
            if padding != 4:
                b64_std += '=' * padding
            
            decoded_bytes = base64.b64decode(b64_std)
            decoded_text = decoded_bytes.decode('utf-8', errors='ignore')
            print(f"  Decoded (urlsafe): {decoded_text[:200]}")
            
            # Look for URLs
            urls_found = re.findall(r'https?://[^\s<>"]+', decoded_text)
            if urls_found:
                print(f"  ✓ Found URLs: {urls_found}")
        except Exception as e:
            print(f"  URLsafe decode failed: {e}")
    
    print("\n  Using decode function:")
    decoded = decode_google_news_url(url)
    if decoded:
        print(f"  ✓ Result: {decoded}")
    else:
        print(f"  ✗ Could not decode")
