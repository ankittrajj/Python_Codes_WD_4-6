import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'bank2')
cursor = con.cursor()
print('Bank Management system ')
acc_no = 101
amt = 0

while True:
    choice = input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Update Account\n5.Account Details\n6.Exit")
    if choice == '1':
        name = input("Enter the name")
        mobile = int(input("Enter the mobile number"))
        age = int(input("Enter the age"))
        amt= int(input('Enter the amt'))
        query = "Insert into cust2 value({},'{}',{},{},{})".format(acc_no,name,mobile,age,amt)
        acc_no = acc_no+1
        cursor.execute(query)
        con.commit()
        print('Open acc successfully!!')

    elif choice == '2':
        amt = input("Enter the amount to deposite")
        acc_no = input("Enter your account no")
        query = "Update cust2 SET amt='{}'+amt where accno='{}'".format(amt, acc_no)
        cursor.execute(query)
        con.commit()
        print("Amount credit successfully")

    elif choice == "3":
        amt = input("Enter the amt to withdraw")
        acc_no = input("Enter the acc no to withdraw")
        query = "Update cust2 SET amt='{}'-amt where accno='{}'".format(amt,acc_no)
        cursor.execute(query)
        con.commit()
        print('Amount Debited')

    # elif choice == '4':
    #     if bal>amt:
    #         print("Deposit amount is :-",amt)
    #     else:
    #         print('Not Deposit!!')

    elif choice =='5':
        acc_no = input('Enter the acc no')
        query = "select * from cust2 where accno = '{}'".format(acc_no)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        con.commit()


    if choice == '6':
        break;




# bug 1----> all my acc have same number.
# bug 2-----> if you are deposit the cash then previous amt is not added.






















# if con.is_connected():
#     print("Connected successfully!!")