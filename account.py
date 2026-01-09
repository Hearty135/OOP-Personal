class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self._balance

# Demonstration
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)  # Create account with owner and initial balance
    account.deposit(500)  # Deposit 500
    account.withdraw(200)  # Withdraw 200
    print(f"Balance for {account.owner}: {account.get_balance()}")  # Print balance

    # Edge case testing
    print("\nTesting edge cases:")
    account.deposit(-100)  # Deposit negative amount
    account.withdraw(2000)  # Withdraw more than balance
    account.withdraw(-50)  # Withdraw negative amount
    account.deposit(0)  # Deposit zero
    account.withdraw(0)  # Withdraw zero
    print(f"Final balance after edge cases: {account.get_balance()}")
