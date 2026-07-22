# Security Architecture - Secure Password Manager


## System Architecture

                USER
                  |
                  |
                  v

          Password Manager CLI

                  |
                  |
              main.py

      +-----------+------------+
      |                        |
      v                        v

Authentication Layer       Password Vault Layer

      |                        |
      v                        v


   auth.py                vault.py


      |                        |
      |                        |
      v                        v

bcrypt Hashing         Encryption Module

                              |
                              |
                              v


                        encryption.py


                              |
                              |
                              v


                       PBKDF2HMAC


                              |
                              |
                              v


                      Fernet Encryption


                              |
                              |
                              v


                      SQLite Database


                 +------------+------------+

                 |                         |

                 v                         v


             users table          passwords table



                 |
                 |
                 v


             audit.py


                 |
                 |
                 v


            audit.log



---

# Authentication Flow


1. User enters username and password.

2. System retrieves stored bcrypt hash.

3. bcrypt verifies password.

4. Successful authentication grants vault access.


Flow:

                    User Password
                        |
                        v
                bcrypt Verification
                        |
                        v
                 User Authentication
                        |
                        v
                   Vault Access


            
---

# Encryption Flow


Stored password protection:

                Website Password
                       |

                       v

                Master Password + Salt
                       |

                       v
                 PBKDF2HMAC

                       |

                       v

                 Encryption Key

                       |

                       v

                 Fernet Encryption

                       |

                       v

                 Encrypted Password Stored


---

# Security Boundaries


## Trust Boundary 1

User Input → Application

Protection:

- Input validation
- Password checking


## Trust Boundary 2

Application → Database

Protection:

- Parameterized queries
- Encryption


## Trust Boundary 3

Database → Stored Credentials

Protection:

- bcrypt hashes
- encrypted passwords






