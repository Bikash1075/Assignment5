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
A=Account("Asish", 5000)
SA=SavingsAccount("Asish", 5000, 5)
print(f"Here, {SA.title} is the title, {SA.balance} is the balance and {SA.InterestRate} is the interestRate.")