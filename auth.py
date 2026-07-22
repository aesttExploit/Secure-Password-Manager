import sqlite3
import bcrypt

DB_NAME = "passwords.db"


def register(username, password):

    if not username.strip() or not password.strip():
        return False, "Username and Password cannot be empty."

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    try:

        cursor.execute("""
            INSERT INTO users (username, password_hash)
            VALUES (?, ?)
        """, (username, password_hash))

        conn.commit()

        return True, "Registration successful!"

    except sqlite3.IntegrityError:

        return False, "Username already exists."

    finally:

        conn.close()


def login(username, password):

    if not username.strip() or not password.strip():
        return None

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, password_hash
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    if user is None:
        return None

    user_id = user[0]
    stored_hash = user[1].encode("utf-8")

    if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
        return user_id

    return None