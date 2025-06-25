from shape import Shape, InvalidDimensionError

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidDimensionError("Width and height must be positive numbers.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle (width={self.width}, height={self.height}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"
    
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    # Arithmetic operations
    def __mul__(self, factor):
        """Scale rectangle by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Rectangle(self.width * factor, self.height * factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __truediv__(self, factor):
        """Scale rectangle by dividing dimensions by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Rectangle(self.width / factor, self.height / factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __pow__(self, power):
        """Raise rectangle's dimensions to a power"""
        if isinstance(power, (int, float)):
            return Rectangle(self.width ** power, self.height ** power)
        return NotImplemented
    
    def __add__(self, other):
        """Add two rectangles by adding their dimensions"""
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        return super().__add__(other)
    
    def __sub__(self, other):
        """Subtract two rectangles by subtracting their dimensions"""
        if isinstance(other, Rectangle):
            new_width = self.width - other.width
            new_height = self.height - other.height
            if new_width <= 0 or new_height <= 0:
                raise ValueError("Resulting dimensions would be non-positive")
            return Rectangle(new_width, new_height)
        return super().__sub__(other)
    
    # Comparison methods specific to rectangles
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return super().__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() < other.get_area()
        return super().__lt__(other)
    
    # Hash method
    def __hash__(self):
        return hash(('Rectangle', self.width, self.height))