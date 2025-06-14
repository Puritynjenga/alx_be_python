class BankAccount:
    def __init__(self,initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount must be positive")  
            return False
        self.account_balance += amount
        return True
    def withdraw(self,amount):
        if amount<=0:
            print("You can not withdraw zero amount")
            return False
        if self.account_balance >= amount:
            self.account_balance-+ amount
            return True
        elif amount> self.account_balance:
            print("Insufficient funds")
        else:
            return False
    def display_balance(self):
            print(f"Your current account balance is: {self.account_balance: .2f}")