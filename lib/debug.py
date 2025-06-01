from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def debug():
    # Example usage
    author1 = Author(name="John Doe")
    author1.save()
    
    magazine1 = Magazine(name="Tech Today", category="Technology")
    magazine1.save()
    
    article1 = Article(title="Python Programming", author_id=author1.id, magazine_id=magazine1.id)
    article1.save()
    
    print(f"Author: {author1.name}")
    print(f"Articles by author: {[a.title for a in author1.articles()]}")
    print(f"Magazines by author: {[m.name for m in author1.magazines()]}")
    
    print(f"\nMagazine: {magazine1.name}")
    print(f"Articles in magazine: {magazine1.article_titles()}")
    print(f"Contributors to magazine: {[a.name for a in magazine1.contributors()]}")

if __name__ == '__main__':
    debug()