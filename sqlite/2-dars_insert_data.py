import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 🔹 Ma’lumot qo‘shish
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Avazbek", 20))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Jasur", 22))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Malika", 19))

print("✅ Ma’lumotlar qo‘shildi!")

conn.commit()
conn.close()
