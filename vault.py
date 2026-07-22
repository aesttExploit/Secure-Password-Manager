import sqlite3
import os

from encryption import encrypt_password, decrypt_password

DB_NAME = "passwords.db"


# ==========================
# CREATE
# ==========================
def save_password(user_id, site, username, password, master_password):

    salt = os.urandom(16)

    encrypted = encrypt_password(
        password,
        master_password,
        salt
    )

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO passwords
        (user_id, site, username, encrypted_password, salt)
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        site,
        username,
        encrypted,
        salt
    ))

    conn.commit()
    conn.close()

    print("Password saved successfully.")


# ==========================
# READ
# ==========================
def view_passwords(user_id, master_password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT site, username, encrypted_password, salt
        FROM passwords
        WHERE user_id = ?
    """, (user_id,))

    rows = cursor.fetchall()

    conn.close()

    if not rows:
        print("No passwords found.")
        return

    print("\n===== SAVED PASSWORDS =====")

    for row in rows:

        site = row[0]
        username = row[1]
        encrypted = row[2]
        salt = row[3]

        password = decrypt_password(
            encrypted,
            master_password,
            salt
        )

        print(f"\nWebsite : {site}")
        print(f"Username : {username}")
        print(f"Password : {password}")


# ==========================
# UPDATE
# ==========================
def update_password(user_id, site, new_password, master_password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id
        FROM passwords
        WHERE user_id = ? AND site = ?
    """, (user_id, site))

    row = cursor.fetchone()

    if row is None:
        print("Website not found.")
        conn.close()
        return

    salt = os.urandom(16)

    encrypted = encrypt_password(
        new_password,
        master_password,
        salt
    )

    cursor.execute("""
        UPDATE passwords
        SET encrypted_password = ?, salt = ?
        WHERE user_id = ? AND site = ?
    """, (
        encrypted,
        salt,
        user_id,
        site
    ))

    conn.commit()
    conn.close()

    print("Password updated successfully.")


# ==========================
# DELETE
# ==========================
def delete_password(user_id, site):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM passwords
        WHERE user_id = ? AND site = ?
    """, (user_id, site))

    conn.commit()

    if cursor.rowcount > 0:
        print("Password deleted successfully.")
    else:
        print("Website not found.")

    conn.close()


    # ==========================
# SEARCH PASSWORD
# ==========================
def search_password(user_id, site, master_password):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT site, username, encrypted_password, salt
        FROM passwords
        WHERE user_id = ? AND site = ?
    """, (user_id, site))

    row = cursor.fetchone()

    conn.close()

    if row is None:
        print("Website not found.")
        return

    password = decrypt_password(
        row[2],
        master_password,
        row[3]
    )

    print("\n===== SEARCH RESULT =====")
    print(f"Website : {row[0]}")
    print(f"Username : {row[1]}")
    print(f"Password : {password}")