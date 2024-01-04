# https://www.w3schools.com/python/python_mysql_getstarted.asp

import mysql.connector

host = 'sql.alextsui.net'
user2 = 'superuser'
password = 'JackyTsui'
database = 'db_temperature'

# connect to mySQL server
mydb = mysql.connector.connect(host=host, user=user2, password=password)

#  a cursor allows row-by-row processing of the result sets
mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(type(x), x)

print('##### SEPARATOR #####')

# connect to a database
mydb = mysql.connector.connect(host=host,
                               user=user2,
                               password=password,
                               database=database)
mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(type(x), x)

print('##### SEPARATOR #####')

#query = "SELECT * FROM tb_Server LIMIT 10"
query = "SELECT timestamp, temperature FROM tb_Server ORDER BY timestamp DESC LIMIT 10"
query = "SELECT timestamp, temperature FROM tb_Server WHERE temperature > 36 ORDER BY timestamp DESC LIMIT 10"

mycursor = mydb.cursor()
mycursor.execute(query)
myresult = mycursor.fetchall()
# myresult = mycursor.fetchone()

for x in myresult:
  print(type(x), x)
