class rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height
        
    @property
    def width(self):
        return f"Width is {self._width}"
    
    @property
    
    def height(self):
       return f"Height is {self._height}"
    
    
r1= rectangle(1.2,44)

print(r1.height)