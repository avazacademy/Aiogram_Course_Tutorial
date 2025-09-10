import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 🔹 C – CREATE (oldinroq INSERT qilingan edi)

# 🔹 R – READ (SELECT bilan ma’lumotlarni olish)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("👥 Foydalanuvchilar ro‘yxati:")
for row in rows:
    print(row)  # (id, name, age)

# 🔹 U – UPDATE (ma’lumotni yangilash)
cursor.execute("UPDATE users SET age = 21 WHERE name = ?", ("Avazbek",))
print("✅ Avazbekning yoshi yangilandi!")
print("👥 Foydalanuvchilar ro‘yxati:")
for row in rows:
    print(row)  
# 🔹 D – DELETE (ma’lumotni o‘chirish)
cursor.execute("DELETE FROM users WHERE name = ?", ("Malika",))
print("❌ Malika bazadan o‘chirildi!")

print("👥 Foydalanuvchilar ro‘yxati:")
for row in rows:
    print(row)  
    
conn.commit()
conn.close()
