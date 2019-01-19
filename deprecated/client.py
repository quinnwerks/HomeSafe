import mysql.connector

mydb = mysql.connector.connect(
  host="",
  user="",
  passwd="",
  database="mydatabase"
)
#Connect to this piece of shit
print("Hello")
print(mydb) 
print("Hello")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)