def sprinkles(func):
    def wrapper():
        print ("Welcome to the shop")
        func()
    return wrapper
@sprinkles
def cream():
    print("Here is your cream")
        
        
cream()