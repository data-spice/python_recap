class bank:
    def acc(self):
        print ("Normal account user")
        
class branch(bank):
    def acc(self):
        print("Premium account user")
        
p1=bank()
p2=branch()

p1.acc()
p2.acc()