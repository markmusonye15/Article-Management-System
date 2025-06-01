from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article

def test_create_magazine():
    """Can create a magazine instance"""
    magazine = Magazine(name="Sports Weekly", category="Sports")
    assert magazine.category == "Sports"

def test_save_magazine():
    """Can save magazine to database"""
    magazine = Magazine(name="Cooking Monthly", category="Food")
    magazine.save()
    assert magazine.id is not None

def test_magazine_articles():
    """Magazine can list its articles"""
    magazine = Magazine(name="Tech News", category="Technology").save()
    author = Author(name="Tech Writer").save()
    
    Article(title="AI Advances", author_id=author.id, magazine_id=magazine.id).save()
    Article(title="New Gadgets", author_id=author.id, magazine_id=magazine.id).save()
    
    assert len(magazine.articles()) == 2

def test_magazine_contributors():
    """Magazine can list its authors"""
    magazine = Magazine(name="Fashion Today", category="Lifestyle").save()
    author1 = Author(name="Style Expert").save()
    author2 = Author(name="Trend Analyst").save()
    
    Article(title="Summer Trends", author_id=author1.id, magazine_id=magazine.id).save()
    Article(title="Winter Styles", author_id=author2.id, magazine_id=magazine.id).save()
    
    contributors = magazine.contributors()
    assert len(contributors) == 2
    assert contributors[0].name in ["Style Expert", "Trend Analyst"]