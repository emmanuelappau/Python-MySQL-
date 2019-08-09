import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# update table, You can update existing records in a table by using the "UPDATE" statement:

#Example
#Overwrite the address column from "Valley 345" to "Canyoun 123":
database = 'mydatabase'
	)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
