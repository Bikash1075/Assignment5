# 
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance=self.balance - amount
        return self.balance
    
    def deposit(self, amount):
       self.balance=self.balance + amount 
       return self.balance
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance*self.interestRate)//100
Ad=Account("Asish",2000)
print(Ad.deposit(500))

Aw=Account("Asish",2000)
print(Aw.withdrawal(500))


Si=SavingsAccount("Asish",2000,5)
print(Si.interestAmount())