class BankAccount():
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self):
        money = int(input('amount of money: '))
        self.balance += money
        return self.balance
    
    def withdraw(self):
        money = int(input('amount of money: '))
        if self.balance >= money:
            self.balance -= money
        else:
            print('insufficient balance')
        return self.balance
    
    