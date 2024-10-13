import math

class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return math.pi*(self.radius**2)
    
    def perimeter(self):
        return 2*math.pi*(self.radius)
    
    
c1=circle(10)
print(c1.area())
print(c1.perimeter())