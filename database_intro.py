# import mysql.connector as c
# con = c.connect(host='localhost',
#                 user='root',
#                 passwd='Ankit@8285',
#                 database = 'python_sql')
#
# cursor = con.cursor()
#
# while True:
#     name = input("Enter the name")
#     age=int(input("Enter the age"))
#     marks=float(input("Enter the marks"))
#
#     query = "Insert into student value('{}',{},{})".format(name,age,marks)
#     cursor.execute(query)
#     con.commit()
#     print('Data enter successfully!!')
#
#     option = input("Press 1 for enter more data and press 2 for exit")
#     if option == '2':
#         break;






import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd ='Ankit@8285',
                database = 'sagar')

cursor = con.cursor()

while True:
    name = input("Enter the name")
    age = int(input("Enter the age"))
    # salary = float(input("Enter the salary"))

    # query = "Insert into emp value ('{}',{},{})".format(name,age,salary)
    query1 = "Update emp set age={} where name='{}'".format(age,name)
    cursor.execute(query1)
    con.commit()
    print("Data Enterd successfully!!")

    choice = int(input("Press 1 for enter more data.\nPress 2 to exit"))
    if choice == 2:
        break;
    else:
        print('invalid input')


# if con.is_connected():
#     print('Connected!!')
# else:
#     print('Not Connected')























# if con.is_connected():
#     print("Connection Successfull.....")
# else:
#     print('Not connected')