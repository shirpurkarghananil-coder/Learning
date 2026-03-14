class BankAccount:
    def __init__(self):
        self.balance = 0  # instance variable

    def deposit(self, amount):
        self.balance += amount  # instance variable

    def withdraw(self, amount):
        try:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient balance")
        except ValueError as e:
            print("Error:", e)
        else:
            print("Withdrawal successful. Current balance:", self.balance)
    
    def get_balance(self):
        return self.balance  # instance variable

# Create an instance of BankAccount
account = BankAccount()
account.deposit(500)
account.withdraw(200)
print("Current balance:", account.get_balance())
account.withdraw(1000)  # This will cause an insufficient balance error