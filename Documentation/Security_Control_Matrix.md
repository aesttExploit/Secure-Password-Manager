# Security Control Matrix

## Project Name

**Secure Password Manager**

---

# Introduction

The Secure Password Manager implements multiple security controls to protect user credentials and sensitive information. These controls are designed to provide authentication, confidentiality, integrity, access control, and monitoring.

This document explains each security control implemented in the project, its purpose, and how it contributes to the overall security of the application.

---

# Security Controls

## 1. Authentication Security

### Security Problem

Unauthorized users should not be able to access another user's password vault.

### Implemented Control

Password Hashing and Secure Verification

### Implementation

**File:** `auth.py`

**Technology Used:**

- bcrypt

### Description

When a user registers, the password is hashed using the bcrypt algorithm before being stored in the database. During login, the entered password is securely compared with the stored hash.

### Security Benefit

- Prevents plaintext password storage.
- Protects user credentials if the database is compromised.
- Makes password recovery from stored hashes extremely difficult.

---

## 2. Password Encryption

### Security Problem

Stored website passwords should remain confidential even if the database is stolen.

### Implemented Control

Password Encryption using Fernet

### Implementation

**File:** `encryption.py`

**Technology Used**

- Fernet
- PBKDF2HMAC
- SHA-256

### Description

Before saving website passwords to the database, the application encrypts them using Fernet encryption. The encryption key is generated dynamically using the user's master password and a randomly generated salt.

### Security Benefit

- Website passwords are stored in encrypted format.
- Attackers cannot directly read stored credentials.
- Encryption keys are never stored permanently.

---

## 3. Key Management

### Security Problem

Encryption keys should not be stored directly inside the application or database.

### Implemented Control

Dynamic Key Derivation

### Implementation

**File:** `encryption.py`

**Technology Used**

- PBKDF2HMAC
- SHA-256

### Description

Instead of storing encryption keys, the application derives a new encryption key every time using the master password and salt.

### Security Benefit

- Eliminates permanent key storage.
- Improves encryption security.
- Reduces the risk of key exposure.

---

## 4. Salt Management

### Security Problem

Using identical encryption parameters can make encrypted passwords easier to analyze.

### Implemented Control

Random Salt Generation

### Implementation

**File:** `vault.py`

**Technology Used**

- `os.urandom(16)`

### Description

A new random salt is generated every time a password is saved or updated.

### Security Benefit

- Produces unique encryption keys.
- Prevents repeated encryption patterns.
- Increases resistance against cryptographic attacks.

---

## 5. Access Control

### Security Problem

Users should only access their own stored credentials.

### Implemented Control

User-Based Authorization

### Implementation

**File:** `vault.py`

### Description

Every database operation filters records using the authenticated user's ID.

Example SQL query:

```sql
SELECT site, username, encrypted_password
FROM passwords
WHERE user_id = ?
```

### Security Benefit

- Prevents unauthorized access to another user's passwords.
- Maintains proper separation of user data.

---

## 6. Database Security

### Security Problem

Attackers may attempt SQL Injection attacks through user input.

### Implemented Control

Parameterized SQL Queries

### Implementation

**Files**

- auth.py
- vault.py

### Description

The application uses SQLite parameterized queries instead of directly inserting user input into SQL statements.

Example:

```python
cursor.execute(
    "SELECT id FROM users WHERE username = ?",
    (username,)
)
```

### Security Benefit

- Prevents SQL Injection.
- Treats user input as data instead of executable SQL.

---

## 7. Password Policy

### Security Problem

Weak passwords are vulnerable to guessing and brute-force attacks.

### Implemented Control

Password Strength Checker

### Implementation

**File:** `password_checker.py`

### Description

The application evaluates passwords using the following criteria:

- Minimum length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Passwords are classified as:

- Weak
- Medium
- Strong

### Security Benefit

- Encourages stronger passwords.
- Reduces the likelihood of weak user credentials.

---

## 8. Secure Password Generation

### Security Problem

Users often create predictable passwords.

### Implemented Control

Cryptographically Secure Password Generator

### Implementation

**File:** `password_generator.py`

**Technology Used**

- Python `secrets` module

### Description

The application generates random passwords using Python's cryptographically secure random number generator.

### Security Benefit

- Generates highly unpredictable passwords.
- Reduces password guessing attacks.
- Encourages unique passwords for different websites.

---

## 9. Brute Force Protection

### Security Problem

Attackers may repeatedly attempt to guess user passwords.

### Implemented Control

Login Attempt Limitation

### Implementation

**File:** `main.py`

### Description

Users are allowed a maximum of three consecutive login attempts. After three failed attempts, the login process is terminated and the event is recorded in the audit log.

### Security Benefit

- Reduces brute-force login attempts.
- Detects repeated authentication failures.

---

## 10. Security Monitoring

### Security Problem

Suspicious activities should be recorded for future investigation.

### Implemented Control

Audit Logging

### Implementation

**File:** `audit.py`

**Log File**

`audit.log`

### Logged Events

- Successful login
- Failed login
- Account lock after multiple failed attempts
- Password creation
- Password update
- Password deletion
- Password search
- User logout

### Security Benefit

- Provides accountability.
- Helps identify suspicious activities.
- Supports incident investigation.

---

# Summary

The Secure Password Manager implements multiple security mechanisms to protect user information throughout authentication, password storage, and password management.

Implemented security controls include:

- bcrypt password hashing
- Secure password verification
- Fernet encryption
- PBKDF2HMAC key derivation
- Random salt generation
- User-based authorization
- SQL Injection prevention
- Password strength validation
- Secure password generation
- Brute-force protection
- Audit logging

These controls work together to improve the confidentiality, integrity, and security of stored credentials while demonstrating secure software development practices.