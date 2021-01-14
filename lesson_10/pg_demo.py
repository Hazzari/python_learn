import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="user",
    password="password",
)

cur = conn.cursor()

cur.execute("INSERT INTO users (username, full_name) VALUES ('sam', 'Sam White');")
conn.commit()

cur.execute("SELECT id, full_name, username FROM users;")
users = cur.fetchall()
print(users)

#
#
conn.close()
