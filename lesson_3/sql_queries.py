import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()

# #1
# cursor.execute('SELECT * FROM artists')

# #2
# cursor.execute('SELECT * FROM artists WHERE Gender = "Female"')

# #3
# cursor.execute('SELECT * FROM artists WHERE "Birth Year"<1900')

# data = cursor.fetchall()
# print(data.__len__())

#4
cursor.execute('SELECT Name FROM artists ORDER BY "Birth Year"')
data = cursor.fetchall()
print(data[0])

conn.commit()