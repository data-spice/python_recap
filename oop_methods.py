class bank:
    def __init__(self,acc_user,acc_balance,acc_type):
        self.__acc_user=acc_user  #Private
        self._acc_balance=acc_balance #Protected
        self.acc_type=acc_type #Public
        
    def display(self):
        return f"Name: {self.__acc_user}\nBalance: {self._acc_balance}\nAccount_Type: {self.acc_type}"
    
    
p1=bank("Victor",5000000,"Private")

print(p1.display())