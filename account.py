import datetime

class Account:
    def __init__(self, account_number, account_holder_name):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        self.transaction_history.append(Transaction("Deposit", amount))
        print(f"Deposit of ${amount} successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transaction_history.append(Transaction("Withdrawal", -amount))
        print(f"Withdrawal of ${amount} successful.")

    def transfer(self, recipient, amount):
        if amount <= 0:
            print("Invalid transfer amount.")
            return
        if amount > self.balance:
            print("Insufficient funds for transfer.")
            return
        self.balance -= amount
        recipient.deposit(amount)
        self.transaction_history.append(Transaction(f"Transfer to {recipient.account_holder_name}", -amount))
        print(f"Transfer of ${amount} to {recipient.account_holder_name} successful.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

    def display_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: ${self.amount}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.credentials = {}

    def create_account(self, account_number, account_holder_name, username, password):
        if account_number in self.accounts:
            print("Account number already exists.")
            return
        account = Account(account_number, account_holder_name)
        self.accounts[account_number] = account
        self.credentials[username] = password
        print("Account created successfully.")

    def log_in(self, username, password):
        if username in self.credentials and self.credentials[username] == password:
            print("Logged in successfully.")
            self.show_logged_in_menu(self.accounts[username])
        else:
            print("Invalid username or password.")

    def show_logged_in_menu(self, account):
        while True:
            print("\nLogged in as:", account.account_holder_name)
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. View Transaction History")
            print("6. Log Out")
            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == "3":
                recipient_account_number = input("Enter recipient's account number: ")
                amount = float(input("Enter transfer amount: "))
                recipient = self.accounts.get(recipient_account_number)
                if recipient:
                    account.transfer(recipient, amount)
                else:
                    print("Recipient account not found.")
            elif choice == "4":
                account.display_balance()
            elif choice == "5":
                account.display_transaction_history()
            elif choice == "6":
                print("Logging out...")
                return
            else:
                print("Invalid choice. Please try again.")

bank = Bank()

while True:
    print("\nWelcome to the Banking Application!")
    print("1. Create Account")
    print("2. Log In")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        account_holder_name = input("Enter account holder name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(account_number, account_holder_name, username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.log_in(username, password)
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
