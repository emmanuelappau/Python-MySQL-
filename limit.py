import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# limit You can limit the number of records returned from the query, by using the "LIMIT" statement:

#Example
#Select the 5 first records in the "customers" table:
database = 'mydatabase'
	)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)