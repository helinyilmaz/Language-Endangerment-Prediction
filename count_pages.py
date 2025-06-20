#!/usr/bin/env python

import requests
import argparse
import sys

def get_wikipedia_page_count(language_code):
    """
    Get the total number of Wikipedia pages for a given language.
    
    Args:
        language_code (str): The language code (e.g., 'en' for English, 'es' for Spanish)
    
    Returns:
        dict: Dictionary containing page count information
    """
    
    # Wikipedia API endpoint for site statistics
    url = f"https://{language_code}.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'meta': 'siteinfo',
        'siprop': 'statistics',
        'format': 'json'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        stats = data['query']['statistics']
        
        return {
            'language_code': language_code,
            'total_pages': stats.get('pages', 0),
            'articles': stats.get('articles', 0),
            'good_articles': stats.get('good', 0),
            'active_users': stats.get('activeusers', 0),
            'edits': stats.get('edits', 0)
        }
        
    except requests.exceptions.RequestException as e:
        return {'error': f"Network error: {e}"}
    except KeyError as e:
        return {'error': f"Data parsing error: {e}"}
    except Exception as e:
        return {'error': f"Unexpected error: {e}"}

def print_wikipedia_stats(stats):
    """Pretty print Wikipedia statistics with enhanced formatting."""
    if 'error' in stats:
        print(f"❌ Error: {stats['error']}")
        return
    
    lang = stats['language_code'].upper()
    
    print("=" * 50)
    print(f"📚 {lang} WIKIPEDIA STATISTICS")
    print("=" * 50)
    print()
    
    # Main statistics
    print(f"🗒️  Total Pages:     {stats['total_pages']:>12,}")
    print(f"📄 Articles:        {stats['articles']:>12,}")
    print(f"⭐ Good Articles:   {stats['good_articles']:>12,}")
    print(f"👥 Active Users:    {stats['active_users']:>12,}")
    print(f"✏️  Total Edits:     {stats['edits']:>12,}")
    print()
    
    # Additional insights
    if stats['total_pages'] > 0:
        article_ratio = (stats['articles'] / stats['total_pages']) * 100
        print(f"📊 Article Ratio:   {article_ratio:>11.1f}%")
    
    if stats['articles'] > 0 and stats['active_users'] > 0:
        articles_per_user = stats['articles'] / stats['active_users']
        print(f"📈 Articles/User:   {articles_per_user:>11.1f}")
    
    print()
    print("=" * 50)

def main():
    """Main function to handle command line arguments and execute the program."""
    parser = argparse.ArgumentParser(
        description="Count Wikipedia pages for a specific language",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python wiki_counter.py en          # English Wikipedia
  python wiki_counter.py es          # Spanish Wikipedia
  python wiki_counter.py fr          # French Wikipedia
  python wiki_counter.py de          # German Wikipedia
  
Common language codes:
  en=English, es=Spanish, fr=French, de=German,
  zh=Chinese, ja=Japanese, ru=Russian, pt=Portuguese
        """
    )
    
    parser.add_argument(
        'language_code',
        help='Wikipedia language code (e.g., en, es, fr, de)'
    )
    
    args = parser.parse_args()
    
    print(f"🔍 Fetching Wikipedia statistics for '{args.language_code}'...")
    print()
    
    stats = get_wikipedia_page_count(args.language_code)
    print_wikipedia_stats(stats)

if __name__ == "__main__":
    main()
