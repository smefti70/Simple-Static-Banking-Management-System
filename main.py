class Bank:
    def __init__(self, username, initial_balance):
        self.username = username
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} TK Deposited Successfully"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return f"{amount} TK Successfully Withdrawn"

user = None

while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter your username: ")
        initial_balance = int(input("Enter your initial balance: "))
        user = Bank(username,initial_balance)
        print(f"Account Created Successfully.\n")
        print(f"Account Holder Name: {user.username}")
        print(f"Account Balance: {user.balance} TK")

    elif choice == 2:
        if user is None:
            print("No account created yet. Please create an account first.")
        else:
            amount = int(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Invalid Amount.")
            else:
                print(user.deposit(amount))

    elif choice == 3:
        if user is None:
            print("No account created yet. Please create an account first.")
        else:
            amount = int(input("Enter the amount to withdraw: "))
            print(user.withdraw(amount))

    elif choice == 4:
        if user is None:
            print("No account created yet. Please create an account first.")
        else:
            print(f"Your current balance is {user.get_balance()} TK.")

    elif choice == 0:
        print("Thanks for using Bank Management System.")
        break

    else:
        print("Invalid choice. Please try again with valid input.")