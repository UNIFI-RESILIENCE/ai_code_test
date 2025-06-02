class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

# Example usage:
if __name__ == "__main__":
    account = BankAccount(100.0)  # Initialize account with $100.00
    print(f"Initial balance: ${account.get_balance():.2f}")

    account.deposit(50.0)  # Deposit $50.00
    account.withdraw(30.0)  # Withdraw $30.00
    account.withdraw(150.0)  # Attempt to withdraw $150.00 (should fail due to insufficient funds)
    print(f"Final balance: ${account.get_balance():.2f}")