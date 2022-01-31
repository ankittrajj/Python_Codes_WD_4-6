import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'student_db')

cursor = con.cursor()

# Update the data!!
marks = int(input('Enter your marks'))
name = input('Enter the name')

query = "Update info set marks={} where name ='{}'".format(marks,name)
cursor.execute(query)
con.commit()

# solving bug
if cursor.rowcount>0:
    print("Updated Successfully......")
else:
    print('No updation')