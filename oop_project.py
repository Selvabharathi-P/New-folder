from bankaccounts import *

John = BankAccounts(1000, "John")
David = BankAccounts(500, "David")

John.get_balance()
John.deposit(500)

David.withdraw(1000)
David.withdraw(50)

John.transfer(100, David)

Amy = SavingsAccount(500, "Amy")
Amy.withdraw(50)

Amy.withdraw(445)

Becca = InterestRewardAcc(1000, "Becca")
Becca.deposit(100)