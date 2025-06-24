from shape import Shape, InvalidDimensionError
from math import sqrt

class Hexagon(Shape):
    def __init__(self, side):
        if side <= 0:
            raise InvalidDimensionError("Side must be a positive number!")
        super().__init__("Hexagon")
        self.side = side
        
    def get_area(self):
        return (3 * sqrt(3) / 2) * self.side ** 2
    
    def get_perimeter(self):
        return 6 * self.side
    
    def __str__(self):
        return f"Hexagon(side={self.side}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"