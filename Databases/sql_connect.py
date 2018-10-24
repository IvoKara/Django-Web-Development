# coding: utf-8

import sqlite3
path = "demodatabase.db"

with sqlite3.connect(path) as connection:
	cursor = connection.cursor()
	cursor.execute("insert into employee(Id, firstname, lastname) values (121212121, 'Lol', 'Lolev');")
	cursor = connection.cursor()
	cursor.execute("select * from employee")
	for i in cursor.fetchall():
		print(i)
	connection.commit()
	connection.close()
