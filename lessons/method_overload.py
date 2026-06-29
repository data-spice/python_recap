class over:
    def sum(self,a,b,c=None):
        if c is None:
            print ("Two numbers")
        else:
            print ("Three numbers")
            
obj=over()

obj.sum(1,2)
obj.sum(2,2,3)