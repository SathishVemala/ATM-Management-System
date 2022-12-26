username='sathish'
password='sathi123'

c_name=input("Enter your name:")
c_pass=str(input("Enter your password:"))

if c_name==username and c_pass==password:
    print('''
    1.Deposit
    2.Withdraw
    3.Ministatement
    4.Exit
    ''')
    amount=50000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("Enter the amount"))
        amount+=dep
        print("Total amount:",amount)
    elif option==2:
        withd=int(input("Enter the amount:"))
        amount-=withd
        print("Total amount:",amount)
    elif option==3:
        print("=======ATM=======")
        print("Username:",username)
        print("Total amount:",amount)
        print("Thanks For Visiting")
        print("==================")
    elif option==4:
        exit()
else:
    print("Please Enter Correct Login Details")


