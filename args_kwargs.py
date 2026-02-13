#args

def greet(*args):
    for name in args:
        print(name , end=" ")


greet("Victor","Shantel","Obunja\n")


#Kwargs

def location(**kwargs):
    for name,address in kwargs.items():
        print(f" Hey {name} do you live in {address}")
    
location (Victor="Kiambu",Shantel="Mombasa")
              
              
#Both args and kwargs

def shipping_address(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    
    for value in kwargs.values():
        print (value, end= " then ")
        
shipping_address("Victor","Mwaniki",school="DeKUT",location="Nyeri county",goods="Nvidia RTX 5090")