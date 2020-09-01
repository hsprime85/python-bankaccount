class BankAccount:		
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.account_balance = balance
    
    def deposit(self, amount):
        self.account_balance += amount

        return self

    def withdraw(self, amount):
        if(self.account_balance - amount) < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance = self.account_balance - 5
        else:    
            self.account_balance -= amount

        return self

    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")

        return self

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance * self.interest_rate

        print(f"interest is ${self.account_balance}")

        return self    

accountA = BankAccount(0.01, 0)
accountB = BankAccount(0.008, 0)

hyunsoo.deposit(1500).deposit(2000).deposit(600).withdraw(3500).display_account_info().yield_interest()
rogers.deposit(500).deposit(2000).withdraw(400).withdraw(500).withdraw(300).withdraw(200).display_account_info().yield_interest()
