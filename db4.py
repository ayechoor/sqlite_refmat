import sqlite3

conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Users WHERE email="csev@umich.edu"')
for row in cur:
     print(row)

cur.execute('SELECT name FROM Users WHERE email LIKE "%umich.edu"')
for row in cur:
     print(row)
     
conn.commit()
conn.close()