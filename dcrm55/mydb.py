# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'mansion199',
    port = '3306',
    database = 'elderco555',

    

	)

# # prepare a cursor object
# cursorObject = dataBase.cursor()

# # Create a database
# cursorObject.execute("CREATE DATABASE elderco5")

print("All Done!")
