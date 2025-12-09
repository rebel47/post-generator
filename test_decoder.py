"""Test the Google News URL decoder"""

import json
from urllib.parse import quote, urlparse
import requests
from bs4 import BeautifulSoup

def get_decoding_params(gn_art_id: str) -> dict:
    # Step 1: fetch Google News internal article page
    resp = requests.get(f"https://news.google.com/rss/articles/{gn_art_id}")
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.text, "lxml")
    div = soup.select_one("c-wiz > div")
    
    return {
        "signature": div.get("data-n-a-sg"),
        "timestamp": div.get("data-n-a-ts"),
        "gn_art_id": gn_art_id,
    }

def decode_urls(articles_params: list) -> list:
    # Step 2: build batchexecute payload
    articles_reqs = [
        [
            "Fbv4je",
            (
                f'[\"garturlreq\",[[\"X\",\"X\",[\"X\",\"X\"],null,null,1,1,\"US:en\",'
                f'null,1,null,null,null,null,null,0,1],\"X\",\"X\",1,[1,1,1],1,1,'
                f'null,0,0,null,0],\"{art["gn_art_id"]}\",{art["timestamp"]},'
                f'\"{art["signature"]}\"]'
            ),
        ]
        for art in articles_params
    ]
    
    payload = f"f.req={quote(json.dumps([articles_reqs]))}"
    headers = {"content-type": "application/x-www-form-urlencoded;charset=UTF-8"}
    
    resp = requests.post(
        "https://news.google.com/_/DotsSplashUi/data/batchexecute",
        headers=headers,
        data=payload,
    )
    resp.raise_for_status()
    
    # Step 3: parse final URLs
    body = resp.text.split("\n\n")[1]
    parsed = json.loads(body)[:-2]
    return [json.loads(item[2])[1] for item in parsed]

def decode_google_news_url(gn_url: str) -> str:
    # convenience wrapper for a single URL
    gn_art_id = urlparse(gn_url).path.split("/")[-1]
    params = get_decoding_params(gn_art_id)
    return decode_urls([params])[0]

# Test with example URL
gn_url = "https://news.google.com/rss/articles/CBMirgFBVV95cUxOQXJRd2d4VWVMQ3dqMl9sV1hCN1drRjdWTFliajRMS1BEXzJsWTM4Ul9qTTdJVlZIU3ZsUkNDakV1TnptMnhpam9yZER0b2tDWmJzSHdSLTRRU0c3NUZ4ancwS0dRb2RIaWtTaE5sSkZaSVA5R05jOFo4Sm0zLTA2a3k5VnZsQWdqWGdzZ20tZ183UGNVLVZHSFFoRVk2Z2RSeHNTSkdyNDR4YldrUlE?oc=5&hl=en-US&gl=US&ceid=US:en"

print("Testing Google News URL decoder...")
print(f"Original URL: {gn_url[:80]}...")
print("\nDecoding...")

try:
    decoded_url = decode_google_news_url(gn_url)
    print(f"✓ Success!")
    print(f"Decoded URL: {decoded_url}")
except Exception as e:
    print(f"✗ Error: {e}")
