import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# selecting wildcard characters.You can also select the records that starts, includes, or ends with a given letter or phrase.

#Use the %  to represent wildcard characters:
database = 'mydatabase'
	)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
