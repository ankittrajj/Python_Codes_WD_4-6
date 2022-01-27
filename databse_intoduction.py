# import mysql.connector as c
# con = c.connect(host="localhost",
#                 user = "root",
#                 passwd = 'Ankit@8285',
#                 database = 'intro')
#
# cursor = con.cursor()
#
# while True:
#     name = input("Enter the name")
#     age = int(input("Enter the age"))
#     marks = int(input("Enter the marks"))
#
#     query = "Insert into student value('{}',{},{})".format(name,age,marks)
#     cursor.execute(query)
#     con.commit()
#     print("Data Entered successfully")
#
#     option = input("Enter your choice\n 1.Enter your data one more time\n 2.Exit\n")
#     if option==2:
#         break
#
#     # else:
#     #     continue
#
# # if con.is_connected():
# #     print("Connect Successfully")
# # else:
# #     print("Not connected")



import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'student_db')

cursor = con.cursor()
while True:
    name = input("Enter your name")
    age = int(input("Enter your age"))
    marks = float(input("Enter your marks"))

    query = "Insert into info values('{}',{},{})".format(name,age,marks)
    cursor.execute(query)
    con.commit()
    print("Data entered successfully")

    option = input("Enter your choice\n 1. Enter more Data\n 2.Exit")
    if option == 2:
        break