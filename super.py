class shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

class circle(shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius
    
class square(shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width
    
class triangle(shape):
    def __init__(self,color,filled,width,height):
        super().__init__(color,filled)
        self.width=width
        self.height=height
        
s1=square("blue",True,400)

print(s1.color)