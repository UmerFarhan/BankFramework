class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}\n")

    def getBalance(self):
        formatted_balance = "${:.2f}".format(self.balance)
        return formatted_balance

    def checkBalance(self):
        print(f"\nYour Balance is {self.getBalance()}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        print(f"New balance = {self.getBalance()}\n")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            print(f"New balance = {self.getBalance()}\n")
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05) 
        print("\nDeposit complete.")
        print(f"New Balance = {self.getBalance()}\n")


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            print(f"New Balance = {self.getBalance()}\n")
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
