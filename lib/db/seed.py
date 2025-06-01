from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    # Clear existing data
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

    # Create authors
    authors = [
        Author(name="Jane Smith"),
        Author(name="John Doe"),
        Author(name="Alice Johnson")
    ]
    for author in authors:
        author.save()

    # Create magazines
    magazines = [
        Magazine(name="Tech Today", category="Technology"),
        Magazine(name="Science Weekly", category="Science"),
        Magazine(name="Business Insider", category="Business")
    ]
    for magazine in magazines:
        magazine.save()

    # Create articles
    articles = [
        Article(title="Python Programming", author_id=authors[0].id, magazine_id=magazines[0].id),
        Article(title="Quantum Computing", author_id=authors[1].id, magazine_id=magazines[1].id),
        Article(title="Startup Funding", author_id=authors[2].id, magazine_id=magazines[2].id),
        Article(title="Web Development Trends", author_id=authors[0].id, magazine_id=magazines[0].id),
        Article(title="AI Ethics", author_id=authors[1].id, magazine_id=magazines[1].id)
    ]
    for article in articles:
        article.save()

    print("Database seeded successfully!")