class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def __str__(self):
        return f"Bank Account: account numer: {self.account_number}, account holder: {self.account_holder} ( balance: Php{self.balance} )"
    
    def deposit(self, amountToDeposit):
        if amountToDeposit <= 0:
            print("Invalid Amount!")
        else:
            self.balance += amountToDeposit
            print("Successfully deposited!")
            print(f"Updated Balance: {self.balance}")
    
    def withdraw(self, amountToWithdraw):
        if amountToWithdraw <= 0:
            print("Invalid Amount!")
        elif amountToWithdraw > self.balance:
            print("Amount entered is higher than the current balance!")
        else:
            self.balance -= amountToWithdraw
            print(f"New Balance: {self.balance}")
        
    def checkBalance(self):
        print(f"Current Balance: {self.balance}")

james_bankAcc = BankAccount(account_number="010002", account_holder="James Conrad", balance=123000)
james_bankAcc.deposit(150000)
james_bankAcc.checkBalance()

james_bankAcc.withdraw(2250000)
james_bankAcc.checkBalance()