class car:
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color
    
    def __str__(self):
        return f"The name of the car is {self.model}"
        
car1=car("Toyota",2024,"Red")
    
print(car1.model)  
print(car1.year)
print(car1.color)  

print (car1)