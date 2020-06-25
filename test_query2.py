import sqlite3
import pandas as pd

conn = sqlite3.connect('student.db')

c = conn.cursor()

c.execute("""
SELECT *
FROM students
""")

students = c.fetchall()

conn.commit()



c.execute("""
SELECT *
FROM classes
""")

classes = c.fetchall()

conn.commit()



c.execute("""
SELECT *
FROM scores
""")

scores = c.fetchall()

conn.commit()

conn.close()

print(pd.DataFrame(students))

print()
print()


print(pd.DataFrame(classes))

print()
print()


print(pd.DataFrame(scores))
