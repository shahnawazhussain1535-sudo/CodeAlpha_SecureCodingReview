"""Safer local login example; educational demonstration, not a complete production auth system."""
import hashlib
import hmac
import secrets
import sqlite3
from pathlib import Path

DB_PATH = Path("secure_demo.db")
ITERATIONS = 300_000

def hash_password(password, salt=None):
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)
    return salt.hex(), digest.hex()

def verify_password(password, salt_hex, expected_hash_hex):
    salt = bytes.fromhex(salt_hex)
    _, actual_hash = hash_password(password, salt)
    return hmac.compare_digest(actual_hash, expected_hash_hex)

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, salt_hex TEXT NOT NULL, password_hash TEXT NOT NULL)")
        exists = conn.execute("SELECT username FROM users WHERE username = ?", ("demo",)).fetchone()
        if exists is None:
            salt_hex, password_hash = hash_password("demo123")
            conn.execute("INSERT INTO users (username, salt_hex, password_hash) VALUES (?, ?, ?)", ("demo", salt_hex, password_hash))

def login(username, password):
    # SAFE: placeholders keep user input separate from SQL syntax.
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute("SELECT salt_hex, password_hash FROM users WHERE username = ?", (username,)).fetchone()
    if row is None:
        return False
    salt_hex, expected_hash = row
    return verify_password(password, salt_hex, expected_hash)

def main():
    init_db()
    print("Local secure demo. Dummy account: demo / demo123")
    username = input("Username: ").strip()
    password = input("Password: ")
    print("Login successful." if login(username, password) else "Invalid username or password.")

if __name__ == "__main__":
    main()
