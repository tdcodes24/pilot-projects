# Python Banking Program


class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amountprint(
            f"Deposited ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds.")
        else:
            self.balance += amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")


user_name = input("Enter your name")
user = user(name=user_name)

print(f"Welcome, {user.name}!")
print(f"Your current balance is: ${user.balance}")


def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")


def deposit():
    try:
        amount = float(input("Enter an amount to be deposited: "))

        if amount < 0:
            print("Thats not a valid amount")
            return 0
        else:
            return amount

    except ValueError:
        print("Please enter a valid number")
        return 0


def withdraw(balance):
    try:
        amount = float(input("Enter amount to be withdrawn: "))

        if amount > balance:
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Amount must be greater than $0")
            return 0
        else:
            return amount
    except ValueError:
        print("Please enter a valid number")
        return 0


def main():

    balance = 0
    is_running = True

    while is_running:
        print("****************")
        print("Banking Program")
        print("*****************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        print("****************")
        choice = input("Enter your choice (1-4): ")
        print("****************")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid function")

    print("Thank you! Have a nice day!")


if __name__ == '__main__':
    main()
