import sqlite3

# Connect to the SQLite database (it will create a new file named 'kapustin.db' if it doesn't exist)
conn = sqlite3.connect('kapustin.db')
cursor = conn.cursor()

# Create the Opera table
cursor.execute('''
CREATE TABLE IF NOT EXISTS works (
    opus_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    type TEXT NOT NULL,
    year INTEGER NOT NULL,
    recording_exists BOOLEAN NOT NULL,
    length TEXT,
    youtube_link TEXT,
    num_instruments INTEGER NOT NULL,
    instruments TEXT,
    num_sections INTEGER NOT NULL,
    section_names TEXT,
    referenced_work TEXT
)
''')

# Create the Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database initialized and tables created!")
