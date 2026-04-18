import sqlite3

# -----------------------------
# INIT DATABASE
# -----------------------------
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    # RESULTS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            department TEXT,
            score REAL,
            verdict TEXT
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# REGISTER USER
# -----------------------------
def register_user(email, password):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, password)
        )

        conn.commit()
        conn.close()
        return True
    except:
        return False


# -----------------------------
# VALIDATE USER
# -----------------------------
def validate_user(email, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user is not None


# -----------------------------
# SAVE RESULT
# -----------------------------
def save_results(email, score, verdict):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            score REAL,
            verdict TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO results (email, score, verdict) VALUES (?, ?, ?)",
        (email, score, verdict)
    )

    conn.commit()
    conn.close()


def get_last_result(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT score, verdict FROM results
        WHERE email=? ORDER BY id DESC LIMIT 1
    """, (email,))

    result = cursor.fetchone()
    conn.close()

    return result