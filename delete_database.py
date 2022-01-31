import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'student_db')

cursor = con.cursor()

# delete the  info from the database
age = int(input("Enter the age"))
query = "delete from info where age = {}".format(age)
cursor.execute(query)
con.commit()

if cursor.rowcount>0:
    print("Data Deleted......")
else:
    print("Invalid Input!!")