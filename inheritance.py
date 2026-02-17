class bank:
    def __init__(self,name,amount,balance):
        self.name= name 
        self.amount=amount
        self.balance=balance
    def loan(self):
         print(f"{self.name} has a loan")
         
class sme(bank):
    
    pass


p1= sme("kk",500,900)

sme.loan(p1)

p1.loan()