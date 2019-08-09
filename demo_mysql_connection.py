import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502'
	)

print(mydb)