import psycopg2

conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "5000",
    host = "localhost",
    port = "5432"
)

cursor = conn.cursor()


# cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, percentage FLOAT)")

# cursor.execute("INSERT INTO students VALUES (3, 'RG', 92.50 )")

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

# conn.commit()
conn.close()