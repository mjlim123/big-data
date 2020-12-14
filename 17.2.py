'''
Name: Marcus Lim
Assignment: 17.2 CURSOR METHOD FETCHALL AND ATTRIBUTE DESCRIPTION

Open the books database and use Cursor method execute to select all the data in the titles
table, then use description and fetchall to display the data in tabular format.
'''
import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM titles")
data = cursor.fetchall()
desc = cursor.description
column_names = []
for i in desc:
    column_names.append(i[0])

df = pd.DataFrame(data, columns=column_names)
print(df)