import sqlite3

#Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#Query data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

#Query certain columns
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

#Insert new rows
new_rows=[('Cats','Cat city','2088.10.17'),
          ('Mens','Men city','2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)    #stores each of them in the same order as question mark
connection.commit()

#Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)