# Threat Model - Secure Password Manager

## 1. Project Overview

The Secure Password Manager is a cybersecurity-focused application designed to securely store and manage user credentials.

The system implements authentication, cryptographic protection, access control, password generation, password strength validation, and security monitoring.

The main security objective is protecting sensitive credentials from unauthorized access and credential theft.

---

# 2. Assets

The following assets require protection:

| Asset | Description |
|---|---|
| User Credentials | Login username and password |
| Stored Website Passwords | User's saved account credentials |
| Master Password | Used to generate encryption keys |
| Encryption Keys | Derived cryptographic keys |
| Database Records | User and vault information |
| Audit Logs | Security activity records |


---

# 3. Threat Actors

## External Attacker

Possible capabilities:

- Database theft
- Password guessing
- SQL injection attempts
- Unauthorized access attempts


## Local Attacker

Possible capabilities:

- Access to local files
- Attempt to read database
- Modify audit logs


## Malicious User

Possible actions:

- Attempt to access another user's vault
- Abuse authentication system


---

# 4. Attack Surface

The application attack surfaces include:

1. Login interface
2. Password vault operations
3. SQLite database
4. Encryption mechanism
5. Audit logging system


---

# 5. Threat Analysis


## Threat 1: Database Theft

### Attack Scenario

An attacker obtains access to passwords.db.

### Impact

Exposure of stored credentials.

### Existing Controls

- Login passwords stored using bcrypt hashing.
- Vault passwords stored using Fernet encryption.
- Encryption keys are not stored.


### Risk

Low


---

## Threat 2: Brute Force Login Attack

### Attack Scenario

An attacker repeatedly attempts login credentials.

### Impact

Possible account compromise.

### Existing Controls

- Maximum 3 login attempts.
- Failed attempts recorded in audit logs.


### Risk

Low-Medium


---

## Threat 3: Weak Password Usage

### Attack Scenario

Users create weak passwords.

Example:

123456
password


### Impact

Credential guessing attacks.


### Existing Controls

- Password strength checker.
- Strong password generator.


### Risk

Reduced


---

## Threat 4: Unauthorized Vault Access

### Attack Scenario

A user attempts to access another user's stored passwords.

### Impact

Credential exposure.


### Existing Controls

- User ID based access control.
- Database foreign key relationship.
- User-specific SQL queries.


### Risk

Low


---

## Threat 5: SQL Injection

### Attack Scenario

Attacker injects SQL commands through input fields.

### Impact

Database compromise.


### Existing Controls

Parameterized SQL queries.

Example:  WHERE username = ?


### Risk

Low


---

## Threat 6: Encryption Key Exposure

### Attack Scenario

Attacker attempts to obtain encryption keys.


### Impact

Vault decryption.


### Existing Controls

- Keys generated dynamically.
- PBKDF2HMAC key derivation.
- Master password never stored.


### Risk

Low


---

# 6. Security Principles Applied


## Confidentiality

Implemented using:

- Fernet encryption
- bcrypt hashing


## Integrity

Implemented using:

- Fernet authentication
- Database constraints


## Availability

Implemented using:

- Error handling
- Controlled database operations


---

# 7. Future Security Improvements

- Multi-factor authentication
- Database-level encryption using SQLCipher
- Persistent account lockout
- Secure audit log storage
- Session timeout mechanism