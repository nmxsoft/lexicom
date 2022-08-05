import sqlite3


conn = sqlite3.connect("db.db")
cursor = conn.cursor()
# Задача 4.1
cursor.execute("""
SELECT * FROM customer a
JOIN city b
on a.cod = b.cod;
               """)
print(cursor.fetchall())
# Задача 4.2
cursor.execute("""
SELECT a.name as person, b.name as city FROM customer a
LEFT JOIN city b
on a.cod = b.cod;
               """)
print(cursor.fetchall())
# Задача 4.3
cursor.execute("""
SELECT a.name as person, b.name as city FROM city b
LEFT JOIN customer a
on a.cod = b.cod;
               """)
print(cursor.fetchall())
