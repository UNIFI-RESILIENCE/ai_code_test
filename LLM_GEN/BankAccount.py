class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

# Example usage
account = BankAccount(1000)  # Create a new account with an initial balance of 1000
account.deposit(500)  # Output: Deposit successful. New balance: 1500
account.withdraw(2000)  # Output: Insufficient funds.
account.withdraw(-100)  # Output: Invalid withdrawal amount. Amount must be positive.
account.withdraw(1000)  # Output: Withdrawal successful. New balance: 500