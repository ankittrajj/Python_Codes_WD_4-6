import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'bank')
cursor = con.cursor()
print('Bank Management system ')
acc_no = 101

while True:
    choice = input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Update Account\n5.Account Details\n6.Exit")
    if choice == '1':
        name = input("Enter the name")
        mobile = int(input("Enter the mobile number"))
        age = int(input("Enter the age"))
        query = "Insert into customer value({},'{}',{},{})".format(acc_no,name,mobile,age)
        acc_no = acc_no+1
        cursor.execute(query)
        con.commit()
        print('Account Created!!')
    if choice == '6':
        break;


























# if con.is_connected():
#     print("Connected successfully!!")