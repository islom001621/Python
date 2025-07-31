# Create a new database with a table named Roster that has three fields: Name, Species, and Age. 
# The Name and Species columns should be text fields, and the Age column should be an integer field.

import sqlite3 

conn=sqlite3.connect('homework_15.db')

cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Roster")
create_table = """
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER 
)
"""

cursor.execute(create_table)
conn.commit()

cursor.execute("SELECT * FROM Roster")
rows = cursor.fetchall()
print("jadvalda---->",  rows)

cursor.close()
conn.close()

jadvalda----> []


# Populate your new table with the following values:

# Name	Species	Age
# Benjamin Sisko	Human	40
# Jadzia Dax	Trill	300
# Kira Nerys	Bajoran	29
import sqlite3

conn = sqlite3.connect('homework_15.db')
cursor = conn.cursor()

insert_table="insert into Roster values ('Benjamin Sisko','Human',40), ('Jadzia Dax','Trill',300),('Kira Nerys','Bajoran',29)"
cursor.execute(insert_table)
cursor.execute('select*from roster')

natija=cursor.fetchall()
print('inserted table', natija)

conn.commit()
cursor.close()
conn.close()

inserted table [('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)]


import sqlite3

conn = sqlite3.connect('homework_15.db')
cursor = conn.cursor()

cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
conn.commit()

cursor.execute("SELECT * FROM Roster")
print(cursor.fetchall())

cursor.close()
conn.close()

[('Benjamin Sisko', 'Human', 40), ('Ezri Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)]

# Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3

conn=sqlite3.connect('homework_15.db')
cursor=conn.cursor()

cursor.execute("select age,name from roster where Species='Bajoran';")
print(cursor.fetchall())

cursor.close()
conn.close()

[(29, 'Kira Nerys')]
