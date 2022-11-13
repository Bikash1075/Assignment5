# Challenge 5
# handling bank account
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance=self.balance - amount
        
    
    def deposit(self, amount):
       self.balance=self.balance + amount 
       
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance*self.interestRate)/100
Ad=SavingsAccount("Asish",2000)
Ad.deposit(500)
Ad.getBalance()
print(Ad.getBalance())

Aw=SavingsAccount("Asish",2000)
Aw.withdrawal(500)
Aw.getBalance()
print(Aw.getBalance())

Si=SavingsAccount("Asish",2000,5)
print(Si.interestAmount())
print("---------------------------------------------")

Ad=Account("Asish",2000)
Ad.deposit(500)
Ad.getBalance()
print(Ad.getBalance())

Aw=Account("Asish",2000)
Aw.withdrawal(500)
Aw.getBalance()
print(Aw.getBalance())

Si=SavingsAccount("Asish",2000,5)
print(Si.interestAmount())