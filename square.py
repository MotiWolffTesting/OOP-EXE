from rectangle import Rectangle
from shape import InvalidDimensionError

class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise InvalidDimensionError("Side must be a positive number!")
        super().__init__(side, side)
        self.name = "Square"
        
    def __str__(self):
        return f"Square (side={self.width}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}."
    
    def __repr__(self):
        return f"Square(side={self.width})"
    
    # Override arithmetic operations for squares
    def __mul__(self, factor):
        """Scale square by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Square(self.width * factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __truediv__(self, factor):
        """Scale square by dividing side by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Square(self.width / factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __pow__(self, power):
        """Raise square's side to a power"""
        if isinstance(power, (int, float)):
            return Square(self.width ** power)
        return NotImplemented
    
    def __add__(self, other):
        """Add two squares by adding their sides"""
        if isinstance(other, Square):
            return Square(self.width + other.width)
        return super().__add__(other)
    
    def __sub__(self, other):
        """Subtract two squares by subtracting their sides"""
        if isinstance(other, Square):
            new_side = self.width - other.width
            if new_side <= 0:
                raise ValueError("Resulting side would be non-positive")
            return Square(new_side)
        return super().__sub__(other)
    
    # Comparison methods specific to squares
    def __eq__(self, other):
        if isinstance(other, Square):
            return self.width == other.width
        return super().__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, Square):
            return self.width < other.width
        return super().__lt__(other)
    
    # Hash method
    def __hash__(self):
        return hash(('Square', self.width))

