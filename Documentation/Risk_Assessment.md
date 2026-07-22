# Risk Assessment

## Project Name

**Secure Password Manager**

---

# Introduction

A risk assessment identifies potential security risks that may affect the password manager and evaluates the security controls implemented to reduce those risks.

The objective of this assessment is to identify possible threats, determine their impact on the application, and recommend improvements where necessary.

---

# Risk Rating

 | Risk Level  |                      Description                                       |
 |-------------|----------------------------------------------------------------------  |
 |  High       |  Serious vulnerability that could significantly compromise the system. |
 |  Medium     |  Moderate risk that should be addressed to improve security.           |
 |  Low        |  Minor risk that is already mitigated or has limited impact.           |

---

# Detailed Risk Analysis

## Risk 1 – Database Theft

### Description

An attacker may obtain a copy of the SQLite database (`passwords.db`).

### Impact

If passwords were stored as plain text, all user credentials would be exposed.

### Existing Controls

- bcrypt password hashing
- Fernet encryption
- PBKDF2HMAC key derivation
- Random salt generation

### Residual Risk

**Low**

---

## Risk 2 – Brute Force Login Attack

### Description

An attacker repeatedly enters different passwords hoping to gain access.

### Existing Controls

- Maximum of three login attempts
- Failed login attempts recorded in `audit.log`

### Residual Risk

**Low**

---

## Risk 3 – SQL Injection

### Description

Attackers may try to inject SQL statements through username or password fields.

Example:

```text
admin' OR '1'='1
```

### Existing Controls

Parameterized SQL queries are used in every database operation.

### Residual Risk

**Low**

---

## Risk 4 – Unauthorized Password Access

### Description

A logged-in user attempts to access another user's stored credentials.

### Existing Controls

Every database query filters records using the authenticated user's ID.

Example:

```sql
WHERE user_id = ?
```

### Residual Risk

**Low**

---

## Risk 5 – Weak Password Selection

### Description

Users may create passwords that are easy to guess.

### Existing Controls

- Password strength checker
- Secure password generator

### Residual Risk

**Medium**

Reason:

The application only informs users about password strength; it does not force them to choose a strong password.

---

## Risk 6 – Encryption Key Exposure

### Description

If encryption keys are stored permanently, attackers may decrypt stored passwords.

### Existing Controls

- Keys are derived using PBKDF2HMAC.
- Keys are generated only when required.
- Keys are never stored in the database.

### Residual Risk

**Low**

---

## Risk 7 – Audit Log Tampering

### Description

The audit log is stored as a normal text file.

An attacker with local system access could modify or delete the log.

### Existing Controls

Activity logging is implemented.

### Residual Risk

**Medium**

---

## Risk 8 – Local Device Compromise

### Description

If the computer running the application is infected with malware, sensitive information may be exposed while the application is running.

### Existing Controls

- Password encryption
- Secure authentication

### Residual Risk

**Medium**

---

# Recommendations

The following improvements can further strengthen the application:

- Implement Multi-Factor Authentication (MFA)
- Enforce strong master password requirements
- Add session timeout after inactivity
- Encrypt the entire SQLite database using SQLCipher
- Digitally sign or hash audit logs to prevent tampering
- Store failed login attempts in the database instead of memory
- Add password history to prevent password reuse
- Automatically back up encrypted vault data

---

# Overall Assessment

The Secure Password Manager implements several important cybersecurity controls that significantly reduce common security risks.

The project demonstrates practical implementation of:

- Secure authentication
- Password hashing
- Data encryption
- Key derivation
- Access control
- SQL Injection prevention
- Brute-force protection
- Audit logging
- Password strength validation
- Secure password generation

Although some advanced enterprise security features are not yet implemented, the current design provides a strong foundation for secure credential management and demonstrates cybersecurity best practices.
