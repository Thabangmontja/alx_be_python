# bank_account.py

class BankAccount:
     # The __init__ method initializes the account balance when a new BankAccount object is created.
     def __init__(self, initial_balance=0):
        # account_balance is a private attribute (indicated by the underscore) to ensure encapsulation
        self._account_balance = initial_balance

    # Method to deposit money into the account
     def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account, only if there are sufficient funds
     def withdraw(self, amount):
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                print(f"Withdrew: ${amount:.2f}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    # Method to display the current account balance
     def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
