# CodeAlpha Cyber Security Internship — Task 3
## Secure Coding Review

### Objective
Review a small Python login example, identify common security weaknesses, and compare it with a safer implementation.

### Files
- `app_vulnerable.py` — intentionally insecure teaching example. Run only locally with dummy data; never use in production.
- `app_secure.py` — safer example using parameterized SQL queries and salted password hashing.
- `SECURE_CODING_REVIEW.md` — findings, risks, fixes, and recommendations.

### Requirements
Python 3.10+; no third-party packages required.

### Run
Open a terminal in this folder and run:
- `python app_vulnerable.py`
- `python app_secure.py`

Both create a local SQLite database. Use only the dummy test account `demo` / `demo123`. Never enter real passwords.

### Main findings
1. SQL query construction by string concatenation can create SQL injection risk.
2. Plain-text password storage exposes passwords if the database is leaked.
3. Different login error messages can reveal whether a username exists.
4. Improvements include parameterized queries, salted password hashing, and generic login errors.

### Disclaimer
For education only. The vulnerable file is intentionally insecure and must never be exposed to the internet or used with real credentials.
