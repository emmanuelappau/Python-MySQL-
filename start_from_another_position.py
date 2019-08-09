import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# offset keyword  If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

#Example
#Start from position 3, and return 5 records:
database = 'mydatabase'
	)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)