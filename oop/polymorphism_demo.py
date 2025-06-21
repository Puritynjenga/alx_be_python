class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")


class Rectangle(Shape):
    def __init__(self,length:float, width:float):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width   
    def __str__(self):
        return f"Rectangle area: {self.area()}"
    
class Circle(Shape):
    def __init__(self,radius:float):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def __str__(self):
        return f"Circle area: {self.area()}"
    

       