class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
        else:
            print("Invalid withdrawal amount.")
    def check_balance(self):
        return self.balance
account = BankAccount(1000)
account.deposit(500)
print(f"Current Balance: {account.check_balance()}")
account.withdraw(200)
print(f"Current Balance: {account.check_balance()}")
account.withdraw(2000)