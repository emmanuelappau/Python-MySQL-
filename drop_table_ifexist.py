import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# drop table if exists, You can delete an existing table by using the "DROP TABLE" statement:
#Example
#Delete the table "customers":
database = 'mydatabase'
	)


mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
