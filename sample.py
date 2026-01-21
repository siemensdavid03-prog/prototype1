import sqlite3
import hashlib

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username varchar(255) NOT NULL,
            password varchar(255) NOT NULL
            ''')

username1, password1 = "admin", hashlib.sha256('password123'.encode()).hexdigest()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username1, password1))

conn.commit()