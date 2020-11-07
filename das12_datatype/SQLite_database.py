import sqlite3
from sqlite3 import Error
import os
import json

# creating a connection to our database
database = os.path.join(os.getcwd(), "film.db")

try:
	conn = sqlite3.connect(database)
except Error as e:
	print(e)

# creating a cursor to execute commands(queries)
curs = conn.cursor()


# TASK_1 write script to find the names of movies which name starts with “B”
curs.execute("SELECT title FROM film WHERE title like 'B%'")
print(curs.fetchall())
conn.commit()


# TASK_2 Write a python code to find the movie which duration is the largest from film table
curs.execute(" SELECT title, max(length) FROM film")
with conn:
	print("\nthe movie which duration is the largest:")
	print(curs.fetchall())



# TASK_3 write a python code to write the data from film table into a json file
a = curs.execute(" SELECT * FROM film")
table_reader = a.fetchall()

with conn:
	print("film table is in python now")
	
# film table is dumbing in json file
with open("film_table.json", "w") as f:
	json.dump(table_reader, f, indent = 2)

print("Film's table is now in JSON file")


# TASK_4  write script which finds all the movies from film table which release date is above 2010 and rate is between 3 and 5 , 
#         after that writes them in a new table called filtered_film

creating_new_table = """CREATE TABLE IF NOT EXISTS filtered_film (
			film_id INT,
			title TEXT,
			description TEXT,
			release_year INT,
			rate REAL,
			length INT,
			special_features TEXT
			);
			"""
curs.execute(creating_new_table)
conn.commit()
				
insert_into_newtable = """INSERT INTO filtered_film (film_id, title, description, release_year, rate, length, special_features)
				SELECT *
				FROM film
				WHERE release_year > 2010 and rate BETWEEN 3 and 5
				ORDER BY film_id
			"""
curs.execute(insert_into_newtable)
conn.commit()
