import pytest
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_test_db():
    """Set up fresh database for each test"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Clear any existing data
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM authors;
        DELETE FROM magazines;
        
        -- Reset autoincrement counters
        DELETE FROM sqlite_sequence WHERE name='authors';
        DELETE FROM sqlite_sequence WHERE name='magazines';
        DELETE FROM sqlite_sequence WHERE name='articles';
    """)
    conn.commit()
    conn.close()