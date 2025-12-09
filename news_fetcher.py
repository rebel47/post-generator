"""
News Fetcher Module
Uses GNews to fetch trending news articles for post generation
"""

from gnews import GNews
from typing import List, Dict, Optional


class NewsFetcher:
    """Fetch news articles using Google News"""
    
    # Available topics
    TOPICS = [
        'WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 
        'SPORTS', 'SCIENCE', 'HEALTH', 'POLITICS', 'CELEBRITIES'
    ]
    
    def __init__(
        self,
        language: str = 'en',
        country: str = 'US',
        period: str = '7d',
        max_results: int = 10
    ):
        """
        Initialize News Fetcher
        
        Args:
            language: Language code (default: 'en')
            country: Country code (default: 'US')
            period: Time period (7d, 1m, 1y, etc.)
            max_results: Maximum number of results
        """
        self.gnews = GNews(
            language=language,
            country=country,
            period=period,
            max_results=max_results
        )
    
    def get_top_news(self) -> List[Dict]:
        """
        Get top news headlines
        
        Returns:
            List of news articles
        """
        try:
            return self.gnews.get_top_news()
        except Exception as e:
            print(f"Error fetching top news: {e}")
            return []
    
    def get_news_by_keyword(self, keyword: str) -> List[Dict]:
        """
        Get news by keyword search
        
        Args:
            keyword: Search keyword
        
        Returns:
            List of news articles
        """
        try:
            return self.gnews.get_news(keyword)
        except Exception as e:
            print(f"Error fetching news for '{keyword}': {e}")
            return []
    
    def get_news_by_topic(self, topic: str) -> List[Dict]:
        """
        Get news by topic
        
        Args:
            topic: Topic name (WORLD, BUSINESS, TECHNOLOGY, etc.)
        
        Returns:
            List of news articles
        """
        try:
            topic_upper = topic.upper()
            if topic_upper not in self.TOPICS:
                print(f"Warning: '{topic}' not in predefined topics list")
            return self.gnews.get_news_by_topic(topic_upper)
        except Exception as e:
            print(f"Error fetching news for topic '{topic}': {e}")
            return []
    
    def get_news_by_location(self, location: str) -> List[Dict]:
        """
        Get news by location
        
        Args:
            location: City/state/country name
        
        Returns:
            List of news articles
        """
        try:
            return self.gnews.get_news_by_location(location)
        except Exception as e:
            print(f"Error fetching news for location '{location}': {e}")
            return []
    
    def get_news_by_site(self, site: str) -> List[Dict]:
        """
        Get news from specific website
        
        Args:
            site: Website domain (e.g., 'cnn.com')
        
        Returns:
            List of news articles
        """
        try:
            return self.gnews.get_news_by_site(site)
        except Exception as e:
            print(f"Error fetching news from site '{site}': {e}")
            return []
    
    def get_articles_for_posts(
        self,
        keyword: Optional[str] = None,
        topic: Optional[str] = None,
        location: Optional[str] = None,
        limit: int = 5
    ) -> List[Dict]:
        """
        Get articles suitable for social media posts
        
        Args:
            keyword: Search by keyword
            topic: Search by topic
            location: Search by location
            limit: Number of articles to return
        
        Returns:
            List of simplified article dictionaries
        """
        articles = []
        
        if keyword:
            articles = self.get_news_by_keyword(keyword)
        elif topic:
            articles = self.get_news_by_topic(topic)
        elif location:
            articles = self.get_news_by_location(location)
        else:
            articles = self.get_top_news()
        
        # Simplify and limit results
        simplified = []
        for article in articles[:limit]:
            simplified.append({
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'url': article.get('url', ''),
                'publisher': article.get('publisher', {}).get('title', 'Unknown') if isinstance(article.get('publisher'), dict) else article.get('publisher', 'Unknown'),
                'published_date': article.get('published date', '')
            })
        
        return simplified
    
    @staticmethod
    def get_available_countries() -> Dict[str, str]:
        """Get list of available countries"""
        return {
            'Australia': 'AU', 'Botswana': 'BW', 'Canada': 'CA', 'Ethiopia': 'ET', 
            'Ghana': 'GH', 'India': 'IN', 'Indonesia': 'ID', 'Ireland': 'IE', 
            'Israel': 'IL', 'Kenya': 'KE', 'Latvia': 'LV', 'Malaysia': 'MY', 
            'Namibia': 'NA', 'New Zealand': 'NZ', 'Nigeria': 'NG', 'Pakistan': 'PK', 
            'Philippines': 'PH', 'Singapore': 'SG', 'South Africa': 'ZA', 'Tanzania': 'TZ', 
            'Uganda': 'UG', 'United Kingdom': 'GB', 'United States': 'US', 'Zimbabwe': 'ZW',
            'Czech Republic': 'CZ', 'Germany': 'DE', 'Austria': 'AT', 'Switzerland': 'CH', 
            'Argentina': 'AR', 'Chile': 'CL', 'Colombia': 'CO', 'Cuba': 'CU', 'Mexico': 'MX', 
            'Peru': 'PE', 'Venezuela': 'VE', 'Belgium': 'BE', 'France': 'FR', 'Morocco': 'MA', 
            'Senegal': 'SN', 'Italy': 'IT', 'Lithuania': 'LT', 'Hungary': 'HU', 
            'Netherlands': 'NL', 'Norway': 'NO', 'Poland': 'PL', 'Brazil': 'BR', 
            'Portugal': 'PT', 'Romania': 'RO', 'Slovakia': 'SK', 'Slovenia': 'SI', 
            'Sweden': 'SE', 'Vietnam': 'VN', 'Turkey': 'TR', 'Greece': 'GR', 'Bulgaria': 'BG', 
            'Russia': 'RU', 'Ukraine': 'UA', 'Serbia': 'RS', 'United Arab Emirates': 'AE', 
            'Saudi Arabia': 'SA', 'Lebanon': 'LB', 'Egypt': 'EG', 'Bangladesh': 'BD', 
            'Thailand': 'TH', 'China': 'CN', 'Taiwan': 'TW', 'Hong Kong': 'HK', 'Japan': 'JP',
            'Republic of Korea': 'KR'
        }
    
    @staticmethod
    def get_available_languages() -> Dict[str, str]:
        """Get list of available languages"""
        return {
            'english': 'en', 'indonesian': 'id', 'czech': 'cs', 'german': 'de', 
            'spanish': 'es-419', 'french': 'fr', 'italian': 'it', 'latvian': 'lv', 
            'lithuanian': 'lt', 'hungarian': 'hu', 'dutch': 'nl', 'norwegian': 'no',
            'polish': 'pl', 'portuguese brasil': 'pt-419', 'portuguese portugal': 'pt-150', 
            'romanian': 'ro', 'slovak': 'sk', 'slovenian': 'sl', 'swedish': 'sv', 
            'vietnamese': 'vi', 'turkish': 'tr', 'greek': 'el', 'bulgarian': 'bg',
            'russian': 'ru', 'serbian': 'sr', 'ukrainian': 'uk', 'hebrew': 'he', 
            'arabic': 'ar', 'marathi': 'mr', 'hindi': 'hi', 'bengali': 'bn', 'tamil': 'ta', 
            'telugu': 'te', 'malyalam': 'ml', 'thai': 'th', 'chinese simplified': 'zh-Hans',
            'chinese traditional': 'zh-Hant', 'japanese': 'ja', 'korean': 'ko'
        }


# Quick helper functions
def get_latest_news(keyword: str = None, max_results: int = 10) -> List[Dict]:
    """
    Quick function to get latest news
    
    Args:
        keyword: Optional search keyword
        max_results: Number of results
    
    Returns:
        List of news articles
    """
    fetcher = NewsFetcher(max_results=max_results)
    if keyword:
        return fetcher.get_news_by_keyword(keyword)
    return fetcher.get_top_news()


def get_article_summary(url: str) -> str:
    """
    Quick function to get article summary
    
    Args:
        url: Article URL
    
    Returns:
        Article summary text
    """
    fetcher = NewsFetcher()
    article = fetcher.get_full_article(url)
    return article.get('summary', article.get('text', ''))


# Example usage
if __name__ == "__main__":
    print("=== News Fetcher Demo ===\n")
    
    # Initialize
    fetcher = NewsFetcher(language='en', country='US', period='7d', max_results=5)
    
    # Get top news
    print("📰 Top News Headlines:")
    top_news = fetcher.get_top_news()
    for i, article in enumerate(top_news[:5], 1):
        print(f"{i}. {article.get('title', 'No title')}")
        print(f"   Publisher: {article.get('publisher', {}).get('title', 'Unknown')}")
        print(f"   URL: {article.get('url', '')}\n")
    
    print("="*60 + "\n")
    
    # Get news by topic
    print("💼 Business News:")
    business_news = fetcher.get_news_by_topic('BUSINESS')
    for i, article in enumerate(business_news[:3], 1):
        print(f"{i}. {article.get('title', 'No title')}")
    
    print("\n" + "="*60 + "\n")
    
    # Get news by keyword
    print("🔍 News about 'AI':")
    ai_news = fetcher.get_news_by_keyword('artificial intelligence')
    for i, article in enumerate(ai_news[:3], 1):
        print(f"{i}. {article.get('title', 'No title')}")
    
    print("\n✅ Demo complete!")
