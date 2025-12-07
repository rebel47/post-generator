"""
Test script for News API endpoints
"""

import requests
import json

BASE_URL = "http://localhost:8000"


def test_top_news():
    """Test top news endpoint"""
    print("=" * 70)
    print("1. Testing GET /news/top")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/news/top", params={
        "country": "US",
        "period": "7d",
        "max_results": 5
    })
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {data['status']}")
        print(f"   Country: {data['country']}")
        print(f"   Articles found: {data['count']}\n")
        
        for i, article in enumerate(data['articles'][:3], 1):
            publisher = article.get('publisher', {})
            publisher_name = publisher.get('title', 'Unknown') if isinstance(publisher, dict) else publisher
            print(f"   {i}. {article.get('title', 'No title')}")
            print(f"      Publisher: {publisher_name}")
            print(f"      URL: {article.get('url', '')[:80]}...")
            print()
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
    print()


def test_search_news():
    """Test news search endpoint"""
    print("=" * 70)
    print("2. Testing GET /news/search")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/news/search", params={
        "keyword": "artificial intelligence",
        "max_results": 5
    })
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {data['status']}")
        print(f"   Keyword: {data['keyword']}")
        print(f"   Articles found: {data['count']}\n")
        
        for i, article in enumerate(data['articles'][:3], 1):
            publisher = article.get('publisher', {})
            publisher_name = publisher.get('title', 'Unknown') if isinstance(publisher, dict) else publisher
            print(f"   {i}. {article.get('title', 'No title')}")
            print(f"      Publisher: {publisher_name}")
            print()
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
    print()


def test_news_by_topic():
    """Test news by topic endpoint"""
    print("=" * 70)
    print("3. Testing GET /news/topic/TECHNOLOGY")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/news/topic/TECHNOLOGY", params={
        "max_results": 5
    })
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {data['status']}")
        print(f"   Topic: {data['topic']}")
        print(f"   Articles found: {data['count']}\n")
        
        for i, article in enumerate(data['articles'][:3], 1):
            publisher = article.get('publisher', {})
            publisher_name = publisher.get('title', 'Unknown') if isinstance(publisher, dict) else publisher
            print(f"   {i}. {article.get('title', 'No title')}")
            print(f"      Publisher: {publisher_name}")
            print()
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
    print()


def test_available_topics():
    """Test available topics endpoint"""
    print("=" * 70)
    print("4. Testing GET /news/topics")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/news/topics")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {data['status']}")
        print(f"   Available topics: {', '.join(data['topics'])}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
    print()


def test_available_countries():
    """Test available countries endpoint"""
    print("=" * 70)
    print("5. Testing GET /news/available-countries")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/news/available-countries")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {data['status']}")
        print(f"   Total countries: {data['count']}")
        
        # Show first 10
        countries = list(data['countries'].items())[:10]
        print(f"   First 10 countries:")
        for name, code in countries:
            print(f"      {name}: {code}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
    print()


def test_news_by_location():
    """Test news by location endpoint"""
    print("=" * 70)
    print("6. Testing GET /news/location")
    print("=" * 70)
    
    response = requests.get(f"{BASE_URL}/news/location", params={
        "location": "New York",
        "max_results": 5
    })
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Status: {data['status']}")
        print(f"   Location: {data['location']}")
        print(f"   Articles found: {data['count']}\n")
        
        for i, article in enumerate(data['articles'][:3], 1):
            publisher = article.get('publisher', {})
            publisher_name = publisher.get('title', 'Unknown') if isinstance(publisher, dict) else publisher
            print(f"   {i}. {article.get('title', 'No title')[:80]}")
            print(f"      Publisher: {publisher_name}")
            print()
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
    print()


if __name__ == "__main__":
    print("\n🚀 Testing News API Endpoints\n")
    
    try:
        test_top_news()
        test_search_news()
        test_news_by_topic()
        test_available_topics()
        test_available_countries()
        test_news_by_location()
        
        print("=" * 70)
        print("✅ All tests completed!")
        print("=" * 70)
        print("\n💡 API Documentation: http://localhost:8000/docs")
        print("🌐 ngrok URL: https://unlicensed-unpopulously-shavonda.ngrok-free.dev")
        print("\n📰 Available News Endpoints:")
        print("   GET /news/top - Get top news headlines")
        print("   GET /news/search?keyword=X - Search news by keyword")
        print("   GET /news/topic/{topic} - Get news by topic")
        print("   GET /news/location?location=X - Get news by location")
        print("   GET /news/site?site=cnn.com - Get news from specific site")
        print("   GET /news/article?url=X - Get full article content")
        print("   GET /news/topics - List available topics")
        print("   GET /news/available-countries - List available countries")
        print("   GET /news/available-languages - List available languages")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API")
        print("Make sure the API is running: python api.py")
    except Exception as e:
        print(f"❌ Error: {e}")
