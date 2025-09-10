import sqlite3

# 🔹 1. Baza bilan ulanish (agar fayl bo‘lmasa, users.db fayl yaratiladi)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 🔹 2. Jadval yaratish
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
""")

print("✅ Baza va jadval yaratildi!")

conn.commit()
conn.close()
