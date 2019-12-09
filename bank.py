class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to our INDIAN BANK")
    def mail(self):
         email=input("Enter the email id:")
    def pas(self):
        pin=input("Enter the password:")
        if(len(pin)>=8):
            print(pin)
        else:
            print("Please enter the correct pin number")
            exit(code)

    def userlogin(self):
        name=input("Enter the  username:")
        for i in name:
            if(ord(i) not in range(65,123)):
                print("Enter the correct name:")
                print(name)
    def mobile(self):
        mob=input("Enter the mobile number")
        if(len(mob)>=10):
            print(mob)
        else:
            print("Please enter the correct mobile number")
            exit(code)
    def accno(self):
        num=input("Enter the account number:")
        if(len(num)>=12):
            print(num)
        else:
            print("Enter the correct account number")
            exit(code)
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n Net Available Balance=", self.balance)
s = Bank_Account()
s.userlogin()
s.mail()
s.pas()
s.mobile()
s.accno()
s.deposit()
s.withdraw()
s.display()
