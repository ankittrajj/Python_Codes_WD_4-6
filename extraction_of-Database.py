import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'student_db')

cursor = con.cursor()

query = 'select * from info'
cursor.execute(query)

# data = cursor.fetchone()
# data1 = cursor.fetchmany(6)
data2 = cursor.fetchall()
print(data2)

#wap to delete the particular info from your data table
# fetch info with the help of fetchone,fetchmany,& fetch all function.
