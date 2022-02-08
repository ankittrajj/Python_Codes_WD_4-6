import mysql.connector as c
con = c.connect(host='localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'bank1')
cursor = con.cursor()
print('Bank Management system ')
acc_no = 101
# amt = 1000

while True:
    choice = input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Update Account\n5.Account Details\n6.Exit")
    if choice == '1':
        name = input("Enter the name")
        mobile = int(input("Enter the mobile number"))
        age = int(input("Enter the age"))
        amt= int(input('Enter the amt'))
        query = "Insert into cust value({},'{}',{},{},{})".format(acc_no,name,mobile,age,amt)
        acc_no = acc_no+1
        cursor.execute(query)
        con.commit()
        print('Account Created!!')
    elif choice == '2':
        amt = int(input("Enter the amt to deposit"))
        query = "UPDATE  cust SET amt={} WHERE acc=101".format(amt)

        acc_no=acc_no+1
        cursor.execute(query)
        con.commit()
        print("Amount deposit Successfully!!")

    elif choice == "3":
        acc_no = int(input("Enter your acc_no: "))
        amnt_wdw = int(input("Enter Amt to Withdraw: "))
        if amnt_wdw > amt:
            print("Invalid Amount")
        else:
            balance = amt - amnt_wdw
            # print(balance)
            query = "UPDATE  cust SET amt={} WHERE acc={}".format(balance, acc_no);
            cursor.execute(query)
            con.commit()
            print("Successfully withdrawal")


    if choice == '6':
        break;


























# if con.is_connected():
#     print("Connected successfully!!")