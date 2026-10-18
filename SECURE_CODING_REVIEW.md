# Secure Coding Review — Task 3

## 1. Purpose
This review compares a deliberately insecure Python login demo with a safer version. It identifies common risks and recommends practical secure-coding improvements.

## 2. Scope and method
- Language: Python
- Database: SQLite
- Method: manual source-code inspection and local functional checks
- Files: `app_vulnerable.py` and `app_secure.py`
- Test data: dummy local account only (`demo` / `demo123`)

## 3. Findings

### Finding 1 — SQL injection risk
**Severity:** High  
**Location:** `app_vulnerable.py`, `login()`

**Issue:** The vulnerable version concatenates username and password into an SQL statement. Input may be interpreted as SQL syntax instead of ordinary data.

**Impact:** A crafted input could change the query meaning and undermine login checks.

**Recommendation:** Use parameterized queries. The secure version uses `?` placeholders and passes values separately.

### Finding 2 — Plain-text password storage
**Severity:** High  
**Location:** `app_vulnerable.py`, `users` table

**Issue:** The vulnerable demo stores the password directly in the database.

**Impact:** Anyone who obtains the database can read the stored password.

**Recommendation:** Store salted password hashes. The secure demo uses PBKDF2-HMAC-SHA256 with a random salt. Production systems should use a vetted authentication framework and a suitable password hashing algorithm such as Argon2id, scrypt, or bcrypt.

### Finding 3 — Authentication error handling
**Severity:** Medium  
**Location:** Login response

**Issue:** Different failure messages may reveal whether a username exists.

**Impact:** This can help an attacker enumerate valid usernames.

**Recommendation:** Use a generic error such as “Invalid username or password.” Production systems should also add rate limiting and monitoring.

## 4. Improvements in the safer example
- Parameterized SQL queries
- Salted password hashing
- Constant-time hash comparison
- Generic authentication failure message
- Dummy local credentials only

## 5. Additional recommendations
1. Never hard-code real passwords, API keys, or secrets in source code.
2. Add rate limiting and monitoring to production login systems.
3. Use HTTPS and secure session handling in web applications.
4. Apply least privilege to database and application accounts.
5. Keep dependencies updated and use automated security checks.
6. Test successful login, wrong password, unknown username, and malformed input.
7. Never log passwords or other sensitive information.

## 6. Basic verification
Run each script locally and try the dummy credentials:
- Username: `demo`
- Password: `demo123`

The secure example should accept these dummy credentials and reject incorrect credentials with a generic error. Do not use real credentials.

## 7. Conclusion
This review demonstrates why user input must be treated as data rather than SQL syntax, and why passwords should not be stored in plain text. Parameterized queries and salted password hashing improve the example.

## 8. References
- OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- OWASP Password Storage Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- Python sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html

## Disclaimer
The vulnerable example is intentionally insecure for local education only. Never expose it to a network or use it with real accounts or passwords.
