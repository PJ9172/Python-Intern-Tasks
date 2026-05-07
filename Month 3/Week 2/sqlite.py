import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, percentage FLOAT)")

cursor.execute("INSERT INTO students VALUES (1, 'PJ', 85.40 )")

conn.commit()
conn.close()