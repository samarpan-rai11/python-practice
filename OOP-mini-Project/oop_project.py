from bank_accounts import *

Samarpan = BankAccount(1000,"Samarpan")
Nepal = BankAccount(10000,"Nepal")

Samarpan.get_balance()

Samarpan.deposit(2000)

Nepal.withdraw(1000)

Nepal.transfer(10,Samarpan)

Jim = InterestReward(1000,"Jim")
Jim.get_balance()
Jim.deposit(100)
Jim.transfer(100, Samarpan)


Blaze = SavingsAcc(1000,"Blaze")
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(1000,Samarpan)
