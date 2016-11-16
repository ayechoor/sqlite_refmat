import sqlite3

conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Users')
cur.execute('CREATE TABLE Users (name VARCHAR(128), email VARCHAR(128))')
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', 
    ('Chuck', 'csev@umich.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', 
    ('Colleen', 'cvl@umich.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', 
    ('Ann', 'ann@msu.edu'))
cur.execute('INSERT INTO Users (name, email) VALUES (?, ?)', 
    ('Yang', 'yang@msu.edu'))
cur.execute('UPDATE Users SET name="Charles" WHERE email="csev@umich.edu"')
cur.execute('SELECT * FROM Users WHERE email="csev@umich.edu"')
for row in cur:
     print(row)

cur.execute('SELECT * FROM Users WHERE email LIKE "%umich.edu"')
for row in cur:
     print(row)
conn.commit()
conn.close()