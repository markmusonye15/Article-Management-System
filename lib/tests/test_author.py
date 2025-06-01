from lib.models.author import Author
from lib.db.connection import get_connection
import pytest

class TestAuthor:
    @classmethod
    def setup_class(cls):
        # Setup test database
        conn = get_connection()
        cursor = conn.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT);
            DELETE FROM authors;
            INSERT INTO authors (name) VALUES ('Test Author');
        """)
        conn.commit()
        conn.close()

    def test_save_author(self):
        author = Author(name="Jane Doe")
        author.save()
        assert author.id is not None

    def test_find_by_id(self):
        author = Author.find_by_id(1)
        assert author.name == "Test Author"