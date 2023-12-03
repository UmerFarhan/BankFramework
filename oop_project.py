from bank_accounts import *
import random

accounts = ["Dave", "John", "Bob", "Dan"]
bank_accounts = {}

def bankAccountsInit():
    for names in accounts:
        bank_accounts[names] = BankAccount(random.randint(500,10000), names)

bankAccountsInit()

def menu():
    options = {1: "Check Balance", 2: "Deposit Money", 3: "Withdraw Money", 4: "Transfer Money", 5: "Exit Program"}
    for index, option in options.items():
        print(index,":",option)
    try:
        user_choice = int(input("Please choose a number from the list:\n"))
        match user_choice:
            case 1:
                user_account.checkBalance()
                menu()
            case 2:
                user_amount = int(input("Type the amount you want to deposit:\n"))
                user_account.deposit(user_amount)
                menu()
            case 3:
                user_amount = int(input("Type the amount you want to withdraw:\n"))
                user_account.withdraw(user_amount)
                menu()
            case 4:
                user_amount = int(input("Type the amount you want to transfer:\n"))
                account_chosen = input("Please type the name of the account you want to transfer to:\n")
                if account_chosen in bank_accounts:
                    user_account.transfer(user_amount, bank_accounts[account_chosen])
                else:
                    print("That account was not found")
                menu()
            case 5:
                exit()
            case _:
                print("\nPlease input a number on the list\n")
                menu()
    except ValueError:
        print("Please keep input to integer numbers only\n")
        menu()

def greeting():
    global user_account
    print("Welcome to Umer's Bank!")
    user_name = input("Please enter your name:\n")
    while True:
        user_account_choice = int(input("Please choose what type of account you would like to create:\n1. Normal Account\n2. Interest Account\n3. Savings Account\n"))
        match user_account_choice:
            case 1:
                user_account = BankAccount(0, user_name)
                break
            case 2:
                user_account = InterestRewardsAcct(0, user_name)
                break
            case 3:
                user_account = SavingsAcct(0, user_name)
                break
            case _:
                print("Please choose a valid option")
                continue
    print(f"\nGreetings {user_name}, what would you like to do today?\n")
    menu()

greeting() 
