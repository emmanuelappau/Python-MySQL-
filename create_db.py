import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502'
	)


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE SHOP")