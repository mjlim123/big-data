'''
Name: Marcus Lim
Assignment: 17.1 BOOKS DATABASE
'''
import pandas as pd
import sqlite3

connection = sqlite3.connect('books.db')

# a. Select all authors' last names from the authors table in descending order.
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))

# b. Select all book titles from the titles table in ascending order.
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

#c. Use INNER JOIN to select all the books for a specific author.
#   Include the title. copyright year and ISBN Order the information alphabetically by title.

print(pd.read_sql('SELECT first, last, title, copyright, isbn FROM authors INNER JOIN titles ORDER BY title ASC ',connection))

# d. Insert a new author into the authors table.

cursor = connection.cursor()
cursor.execute("INSERT INTO authors (first, last) VALUES ('Tony','Gaddis')")
print(pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']))

# e. Insert a new title for an author. Remember that the book must have an
# entry in the author_ISBN table and an entry in the titles table.

cursor.execute("INSERT INTO titles (title, isbn, edition, copyright) VALUES "
               "('Programming Logic And Design','0134801156','5','2019')")
cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES ('6','0134801156')")
print(pd.read_sql("SELECT * FROM titles", connection))
print(pd.read_sql("SELECT * from author_ISBN", connection))

