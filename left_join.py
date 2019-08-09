import mysql.connector

mydb = mysql.connector.connect(
host = 'localhost',
user = 'root',
passwd = '#theresa502',
# left join In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.

#If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:
database = 'mydatabase'
	)	

sql = "SELECT \
	users.name AS user, \
	products.name AS favorite \
	FROM users \
	EFT JOIN products ON users.fav = products.id"
