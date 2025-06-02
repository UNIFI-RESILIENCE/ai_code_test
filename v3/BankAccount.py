# Define the BankAccount class
class BankAccount:
    # Initialize the bank account with an optional starting balance
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    # Method to deposit a specified amount into the bank account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}, New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    # Method to withdraw a specified amount from the bank account
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}, New Balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    # Method to return the current balance of the bank account
    def get_balance(self):
        return self.balance

# Example usage:
account = BankAccount(100)  # Create a bank account with an initial balance of $100
account.deposit(50)         # Deposit $50
account.withdraw(30)        # Withdraw $30
print("Current Balance:", account.get_balance())  # Print the current balance