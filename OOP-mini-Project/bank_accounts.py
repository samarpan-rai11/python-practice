class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}'")  

    def get_balance(self):
        print(f"\nAccount '{self.name}' has Balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance += amount
        print("\nDeposit Complete.")
        self.get_balance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw Complete")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}") 

    def transfer(self,amount,acc):
        try:
            print("\n***********************\n\nBeginning Transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            acc.deposit(amount)
            print("\nTransfer complete! ✅\n\n*********************")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestReward(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete.")
        self.get_balance()


class SavingsAcc(InterestReward):
    def __init__(self,initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithrdraw interrupred: {error}")
    

