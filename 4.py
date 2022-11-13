# Parent and child class
class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0,InterestRate=0):
        super().__init__(title, balance)
        self.title=title
        self.balance=balance
        self.InterestRate=InterestRate

print("Account Details")
A=Account("Asish", 5000)
print(f"Name of the Account Holder is {A.title}")
print(f"Available Balance is {A.balance} Rs")
print(f"Here, {A.title} is the title, {A.balance} is the balance . ")
print("--------------------------------------------------------------")
print("Savings Account Details")
SA=SavingsAccount("Asish", 5000, 5)
print(f"Name of the Account Holder is {SA.title}")
print(f"Available Balance is {SA.balance} Rs")
print(f"Name of the Account Holder is {A.title}")
print(f"Interest Rate on Current Balance in percent is {SA.InterestRate}")
print(f"Here, {SA.title} is the title, {SA.balance} is the balance and {SA.InterestRate} is the interestRate .")