import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# prevent sql injection, When query values are provided by the user, you should escape the values.

#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

#The mysql.connector module has methods to escape query values:
database = 'mydatabase'
	)


mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)