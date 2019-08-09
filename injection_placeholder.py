import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# injection placeholder It is considered a good practice to escape the values of any query, also in update statements.

#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

#The mysql.connector module uses the placeholder %s to escape values in the delete statement:
database = 'mydatabase'
	)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")