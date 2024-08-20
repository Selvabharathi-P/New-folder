class BalanceException(Exception):
    pass

class BankAccounts:
    def __init__(self, amount, name):
        self.balance = amount
        self.name = name
        print(f"Account created✅.")
        print(f"\nAccount '{self.name}'. \n Balance = ${self.balance}.\n ")

    def get_balance(self):
        print(f"\nAccount '{self.name}'. \n Balance = ${self.balance}.\n\n ")

    def deposit(self, amount ):
        self.balance += amount
        print(f"Deposit Completed✅.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"OOPS... Sorry... Your account '{self.name}' has only a balance of ${self.balance}.")
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"Withdrawal Completed✅.")
            self.get_balance()
        except Exception as error:
            print(f"Withdrawal Failed❌: {error}\n\n")

    def transfer(self, amount, name):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"Withdrawal Completed✅.")
            name.deposit(amount)
            print(f"Transfer Completed✅.\n\n")
            self.get_balance()
        except Exception as error:
            print(f"Trancfer Failed❌: {error}\n\n")

class InterestRewardAcc(BankAccounts):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print(f"Deposit Completed✅.")
        self.get_balance()

class SavingsAccount(InterestRewardAcc):
    def __init__(self, amount, name):
        super().__init__(amount, name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(f"Withdrawal Completed✅.")
            self.get_balance()
        except Exception as error:
            print(f"Withdrawal Failed❌: {error}\n\n")
            
