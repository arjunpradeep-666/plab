class bankaccount:
    def __init__(self,name,acc_no,acc_type,balance=0.0):
        self.name=name
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"\n Deposited {amount}.Newbalnce:{self.balance}")
        else:
            print("\n Deposited amount must be positive!")
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
            print(f"\n withdraw{amount}.Remaining balance:{self.balance}")
        elif amount > self.balance:
            print("\n Insufficient balance !")
        else:
            print("\n Invalid withdrawl amount!")
    def display(self):
        print("\n ---Account Details---")
        print(f"Account holder:{self.name}")
        print(f"Account number:{self.acc_no}")
        print(f"Account type:{self.acc_type}")
        print(f"balance:{self.balance}")
        
        
name=input("enter the account holder name:")
acc_no=input("enter the account number:")
acc_type=input("enter the account type:")
initialbalance=float(input("enter the initial balance:"))
account=bankaccount(name,acc_no,acc_type,initialbalance)
account.display()
account.deposit(float(input("\n enter amount to deposit:")))
account.withdraw(float(input("\n enter amount to withdraw:")))
account.display()
        