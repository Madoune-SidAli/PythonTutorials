#install mysql package
import pymysql

#Connecting to Database
mybd = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dbName"
)
mycursor = mybd.cursor()

#CREATE Table
mycursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT )"""

mycursor.execute(sql)

#Insert data
sql ="INSERT INTO EMPLOYEE(FIRST_NAME, \
   LAST_NAME, AGE, SEX, INCOME) \
   VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
   ('Madoune', 'Sid Ali', 24, 'M', 2000)
try:

    mycursor.execute(sql)
    mybd.commit()
except:
   # Rollback in case there is any error
   mybd.rollback()
#Selecting Data from Database
mycursor.execute("SELECT * FROM EMPLOYEE")
#you can use fetchone() to select the first item
myresult = mycursor.fetchall()

for row in myresult:
    print(row)
#
# #Update data
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   mycursor.execute(sql)
   mybd.commit()
except:
   mydb.rollback()
#
# #Selecting Data from Database
mycursor.execute("SELECT * FROM EMPLOYEE")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
#
# #Delete Data
sql = "DELETE FROM EMPLOYEE WHERE  AGE > '%d'" % (20)
try:
   # Execute the SQL command
   mycursor.execute(sql)
   mybd.commit()
except:
   # Rollback in case there is any error
   mybd.rollback()
#
# #Selecting Data from Database
mycursor.execute("SELECT * FROM EMPLOYEE")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

# disconnect from server
mybd.close()