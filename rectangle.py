from shape import Shape, InvalidDimensionError

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidDimensionError("Width and height must be positive numbers.")
        super.__init__("Rectangle")
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def display_info(self):
        return f"Rectangle (width={self.width}, height={self.height}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():2f}"