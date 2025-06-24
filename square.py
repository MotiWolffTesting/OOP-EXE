from rectangle import Rectangle
from shape import InvalidDimensionError

class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise InvalidDimensionError("Side must be a positive number!")
        super().__init__(side, side)
        self.name = "Square"
        
    def display_info(self):
        return f"Square (side={self.width}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}."

