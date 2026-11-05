import mysql.connector 
import pandas as pd

my_conn = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "root",
    database = "Company"
)

if my_conn.is_connected():
    print("SYNDESI")

my_cursor = my_conn.cursor()
# fernoume ta data , alla den ta exoume deiskei
my_cursor.execute('''SELECT * FROM EMPLOYEES WHERE LASTNAME LIKE 'Α%' ''') 
rec = my_cursor.fetchall()
print(rec)

for x in rec:
    print (x)

query ="Select * from Employees"
df = pd.read_sql(query,my_conn)
print(df)

print(df.info())
print(df.describe())


# my_state="INSERT INTO DEPARTMENTS(depid, depname, manager) VALUES (%s, %s, %s)"
# val=(10, 'new_department',999)

# my_cursor.execute(my_state, val)
# my_conn.commit()




my_new_cursor = my_conn.cursor()
my_new_cursor.execute('select * from departments') 
rec = my_cursor.fetchall()

for row in rec:
    print (row)

my_new_cursor2 = my_conn.cursor()
stat2 = "Update employees set salary=%s where empid=%s"
val = (2000, 109)
my_new_cursor2.execute(stat2, val)
my_conn.commit()








