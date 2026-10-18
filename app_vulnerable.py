"""INTENTIONALLY VULNERABLE teaching example. Local dummy data only; never use in production."""
import sqlite3
from pathlib import Path

DB_PATH = Path("vulnerable_demo.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT NOT NULL)")
        conn.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('demo', 'demo123')")

def login(username, password):
    # VULNERABILITY: input is concatenated into SQL. Shown for review only.
    query = "SELECT username FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(query).fetchone() is not None

def main():
    init_db()
    print("Local vulnerable demo. Dummy account: demo / demo123")
    username = input("Username: ")
    password = input("Password: ")
    print("Login successful." if login(username, password) else "Login failed.")

if __name__ == "__main__":
    main()
