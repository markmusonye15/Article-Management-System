from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    print("🌟 Running Simple Queries 🌟")
    
    # Clear old data
    for model in [Article, Author, Magazine]:
        for item in model.find_all():
            item.delete()

    # Create sample data
    author = Author(name="John Doe")
    author.save()

    magazine = Magazine(name="Simple Times", category="News")
    magazine.save()

    article = Article(title="My First Article", 
                     author_id=author.id, 
                     magazine_id=magazine.id)
    article.save()

    # Basic queries
    print("\n📝 All Authors:")
    for a in Author.find_all():
        print(f"- {a.name}")

    print("\n📰 All Magazines:")
    for m in Magazine.find_all():
        print(f"- {m.name} ({m.category})")

    print("\n📄 All Articles:")
    for art in Article.find_all():
        print(f"- '{art.title}' by {art.author().name} in {art.magazine().name}")

if __name__ == "__main__":
    main()