import sqlite3

conn = sqlite3.connect('student.db')

c = conn.cursor()

c.execute("INSERT INTO students VALUES (000001, 'name@site.com', 'Tim', 'Copeland', '10041993')")

conn.commit()

conn.close()
