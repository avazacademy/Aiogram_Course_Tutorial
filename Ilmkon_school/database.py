import sqlite3

def create_db():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_id INTEGER,
            first_name TEXT,
            last_name TEXT,
            FOREIGN KEY (class_id) REFERENCES classes (id)
        )
    """)

    conn.commit()
    conn.close()

def add_class(name: str):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO classes (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_classes():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM classes")
    classes = cursor.fetchall()
    conn.close()
    return classes

def add_student(class_id: int, first_name: str, last_name: str):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (class_id, first_name, last_name) VALUES (?, ?, ?)",
                   (class_id, first_name, last_name))
    conn.commit()
    conn.close()

def get_students_by_class(class_id: int):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, last_name FROM students WHERE class_id=?", (class_id,))
    students = cursor.fetchall()
    conn.close()
    return students
