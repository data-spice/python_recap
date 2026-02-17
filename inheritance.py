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

# sme.loan(p1)
# # p1.loan()



# Multiple inheritance


class developer:
    def __init__(self,language,**kwargs):
        super().__init__(**kwargs)
        self.language=language
    
    def write_code(self):
        print(f"Writing code in {self.language}")
        

class manager:
    def __init__(self,team_size,**kwargs):
        super().__init__(**kwargs)
        self.team_size=team_size
        
    def conduct_meeting(self):
        print(f"Conducting a meeting with {self.team_size} team members")
        
class TeachLead(developer,manager):
    def __init__(self, name,language,team_size):
        super().__init__(language=language,team_size=team_size)
        self.name=name
        
        
    
    def show_role(self):
        print(f"{self.name} is both a developer and a manager.")
        
l1=TeachLead("Victor","python",600)

l1.show_role()
