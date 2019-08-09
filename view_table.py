import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="#theresa502",
 # SELECTING A DATABASE TO CONNECT TO
 database = 'mydatabase'
)

mycursor = mydb.cursor()

# THIS CODE IS USED FOR CREATING A TABLE NAMED [customers]
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# THIS LINE OF CODE SHOWS THE TABLE [customers] IN MYDATABASE
mycursor.execute('SELECT *FROM customers ')
for x in mycursor:
    print(x)
