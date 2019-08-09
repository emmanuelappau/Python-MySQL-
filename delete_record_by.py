import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# delect record by, You can delete records from an existing table by using the "DELETE FROM" statement:

#Delete any record where the address is "Mountain 21":
database = 'mydatabase'
	)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")