from rectangle import Rectangle
from shape import InvalidDimensionError
from math import sqrt

class Triangle(Rectangle):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise InvalidDimensionError("Base and height must be positive numbers!")
        super().__init__(base, height)
        self.name = "Triangle"
        
    
    def get_area(self):
        return 0.5 * self.width * self.height
    
    def get_perimeter(self):
        
        side = sqrt((self.width / 2) ** 2 + self.height ** 2)
        return self.width + 2 * side
    
    def display_info(self):
        return f"Triangle(base={self.width}, height={self.height}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"