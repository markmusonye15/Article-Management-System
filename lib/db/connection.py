import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'articles.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enable access by column name
    
    # Create tables with proper error handling
    try:
        cursor = conn.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                FOREIGN KEY (author_id) REFERENCES authors(id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(id)
            );
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
        raise
    
    return conn