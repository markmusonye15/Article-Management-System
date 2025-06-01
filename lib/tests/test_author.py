from lib.models.author import Author
from lib.db.connection import get_connection

def test_create_author():
    """Can create an author instance"""
    author = Author(name="Ernest Hemingway")
    assert author.name == "Ernest Hemingway"

def test_save_author():
    """Can save an author to database"""
    author = Author(name="Jane Austen")
    author.save()
    assert author.id is not None  # Should get database ID

def test_find_author():
    """Can find an author by ID"""
    author = Author(name="Agatha Christie")
    author.save()
    
    found = Author.find_by_id(author.id)
    assert found.name == "Agatha Christie"

def test_author_articles_empty():
    """New author has no articles"""
    author = Author(name="New Writer")
    author.save()
    assert len(author.articles()) == 0

def test_delete_author():
    """Can delete an author"""
    author = Author(name="Temporary Author")
    author.save()
    author.delete()
    assert Author.find_by_id(author.id) is None