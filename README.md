# 🔐 Secure Password Manager

A command-line based Secure Password Manager developed in Python to demonstrate practical cybersecurity concepts such as authentication, password hashing, encryption, access control, audit logging, and secure password management.

This project was developed as part of my cybersecurity learning journey to apply secure coding practices and understand how password managers protect sensitive credentials.

---

# 📌 Project Objectives

The main objectives of this project are:

- Store website passwords securely
- Protect user credentials using strong cryptography
- Prevent common security attacks
- Demonstrate secure software development practices
- Apply cybersecurity concepts in a practical project

---

# ✨ Features

- User Registration
- Secure Login Authentication
- Password Hashing using bcrypt
- Password Encryption using Fernet
- PBKDF2HMAC Key Derivation
- Secure Password Storage
- Password Strength Checker
- Secure Password Generator
- Search Stored Passwords
- Update Passwords
- Delete Passwords
- Audit Logging
- Brute Force Protection
- SQLite Database

---

# 🛠 Technologies Used

- Python 3
- SQLite
- bcrypt
- cryptography (Fernet)
- PBKDF2HMAC
- SHA-256
- Python secrets module
- Regular Expressions (re)

---

# 📂 Project Structure

```
Password_Manager/
│
├── main.py
├── auth.py
├── vault.py
├── encryption.py
├── database.py
├── audit.py
├── password_checker.py
├── password_generator.py
├── passwords.db
├── audit.log
│
└── Documentation/
    ├── Threat_Model.md
    ├── Security_Architecture.md
    ├── Security_Control_Matrix.md
    └── Risk_Assessment.md
```

---

# 🔒 Security Features

## User Authentication

- Passwords are hashed using **bcrypt** before being stored.
- Password verification is performed securely using bcrypt.

---

## Password Encryption

Website passwords are encrypted before storage using:

- Fernet Encryption
- PBKDF2HMAC
- SHA-256
- Random Salt

This ensures passwords remain unreadable even if the database is compromised.

---

## Password Strength Validation

The application evaluates password strength based on:

- Minimum length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Passwords are classified as:

- Weak
- Medium
- Strong

---

## Secure Password Generation

The application generates random passwords using Python's **secrets** module, providing cryptographically secure randomness.

---

## SQL Injection Prevention

All database queries use parameterized SQL statements to prevent SQL Injection attacks.

Example:

```python
cursor.execute(
    "SELECT * FROM users WHERE username=?",
    (username,)
)
```

---

## Brute Force Protection

The application limits login attempts to three consecutive failures before returning the user to the main menu.

---

## Audit Logging

The following security events are recorded in `audit.log`:

- Successful Login
- Failed Login
- Account Lock
- Password Creation
- Password Update
- Password Deletion
- Password Search
- User Logout

---

# 🗄 Database Design

The project uses SQLite with two tables:

## Users Table

Stores:

- User ID
- Username
- Password Hash
- Registration Date

## Passwords Table

Stores:

- Website
- Username
- Encrypted Password
- Salt
- Creation Date

---

# ▶️ How to Run

## Clone the repository

```bash
git clone <repository-url>
```

## Install dependencies

```bash
pip install bcrypt cryptography
```

## Initialize the database

```bash
python database.py
```

## Run the application

```bash
python main.py
```

---

# 📖 Documentation

Additional documentation is available in the `Documentation` folder:

- Threat Model
- Security Architecture
- Security Control Matrix
- Risk Assessment

---

# 🚀 Future Improvements

- Multi-Factor Authentication (MFA)
- SQLCipher Database Encryption
- Session Timeout
- Password History
- Automatic Backup
- Password Expiry Notifications
- GUI using Tkinter or PyQt
- Secure Cloud Synchronization

---

# 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- Secure Authentication
- Password Hashing
- Cryptography
- Key Derivation
- Secure Password Storage
- Access Control
- Audit Logging
- SQL Injection Prevention
- Python Security Libraries
- Secure Software Development

---

# 📜 License

This project was developed for educational and portfolio purposes.

# Disclaimer

This project was developed for educational and cybersecurity learning purposes.
It demonstrates security concepts such as encryption, authentication, and secure storage.
It has not undergone a professional security audit and should not be used for storing real credentials.
