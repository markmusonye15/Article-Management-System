from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_create_article():
    """Can create an article instance"""
    article = Article(title="Python Tips", author_id=1, magazine_id=1)
    assert article.title == "Python Tips"

def test_save_article():
    """Can save article to database"""
    author = Author(name="Tech Writer").save()
    magazine = Magazine(name="Code Weekly", category="Programming").save()
    
    article = Article(title="Debugging Guide", author_id=author.id, magazine_id=magazine.id)
    article.save()
    assert article.id is not None

def test_find_article():
    """Can find article by title"""
    Article(title="Find Me", author_id=1, magazine_id=1).save()
    found = Article.find_by_title("Find Me")
    assert found is not None

def test_article_relationships():
    """Article can find its author and magazine"""
    author = Author(name="Science Writer").save()
    magazine = Magazine(name="Science Today", category="Science").save()
    article = Article(title="Lab Results", author_id=author.id, magazine_id=magazine.id).save()
    
    assert article.author().name == "Science Writer"
    assert article.magazine().name == "Science Today"