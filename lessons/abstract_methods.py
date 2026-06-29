from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def generate_statement(self):
        pass
    
class ShariaCompliance(ABC):

    @abstractmethod
    def calculate_profit_share(self):
        pass
    
class DigitalWallet(ABC):

    @abstractmethod
    def authenticate_transaction(self):
        pass
    
class InvestmentPortfolio(ABC):

    @abstractmethod
    def calculate_returns(self):
        pass
    
class PremiumIslamicDigitalInvestmentAccount(
    Account,
    ShariaCompliance,
    DigitalWallet,
    InvestmentPortfolio
):

    def __init__(self, balance):
        self.balance = balance

    # Account methods
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient funds")

    def generate_statement(self):
        print("Current Balance:", self.balance)

    # Sharia Compliance
    def calculate_profit_share(self):
        profit = self.balance * 0.1
        print("Profit Share:", profit)

    # Digital Wallet
    def authenticate_transaction(self):
        print("Transaction authenticated via OTP")

    # Investment Portfolio
    def calculate_returns(self):
        returns = self.balance * 0.15
        print("Investment Returns:", returns)
        
        
account = PremiumIslamicDigitalInvestmentAccount(10000)

account.deposit(2000)
account.withdraw(1500)
account.generate_statement()
account.calculate_profit_share()
account.authenticate_transaction()
account.calculate_returns()