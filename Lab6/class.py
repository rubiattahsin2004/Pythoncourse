class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Tk. {amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Tk. {amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: Tk. {self.balance}")


account = BankAccount(
    "123456789",
    10000,
    "03-08-2026",
    "Rubiat Tahsin"
)

# Calling methods
account.deposit(5000)
account.withdraw(2000)
account.check_balance()
