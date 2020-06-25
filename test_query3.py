import sqlite3
import pandas as pd

conn = sqlite3.connect('student.db')

c = conn.cursor()

c.execute("""
SELECT *
FROM students
""")

result = c.fetchall()

conn.commit()
conn.close()

print(result)

print(pd.DataFrame(result))
