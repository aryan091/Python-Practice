# Create a class Rectangle with methods to calculate the area and perimeter. Then create two objects of this class and calculate their area and perimeter.

class Rectangle:
    def __init__(self ,width , length):
        self.width = width
        self.length = length
        
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2*(self.width + self.length)
    
    

rec1 = Rectangle(10 , 20)
rec2 = Rectangle(15 , 30)

print(rec1.area())
print(rec1.perimeter())

print(rec2.area())
print(rec2.perimeter())