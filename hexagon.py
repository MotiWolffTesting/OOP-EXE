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
    
    def __repr__(self):
        return f"Hexagon(side={self.side})"
    
    # Arithmetic operations
    def __mul__(self, factor):
        """Scale hexagon by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Hexagon(self.side * factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __truediv__(self, factor):
        """Scale hexagon by dividing side by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Hexagon(self.side / factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    # Power operator
    def __pow__(self, power):
        """Raise hexagon's side to a power"""
        if isinstance(power, (int, float)):
            return Hexagon(self.side ** power)
        return NotImplemented
    
    def __add__(self, other):
        """Add two hexagons by adding their sides"""
        if isinstance(other, Hexagon):
            return Hexagon(self.side + other.side)
        return super().__add__(other)
    
    def __sub__(self, other):
        """Subtract two hexagons by subtracting their sides"""
        if isinstance(other, Hexagon):
            new_side = self.side - other.side
            if new_side <= 0:
                raise ValueError("Resulting side would be non-positive")
            return Hexagon(new_side)
        return super().__sub__(other)
    
    # Comparison methods specific to hexagons
    def __eq__(self, other):
        if isinstance(other, Hexagon):
            return self.side == other.side
        return super().__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, Hexagon):
            return self.side < other.side
        return super().__lt__(other)
    
    # Hash method
    def __hash__(self):
        return hash(('Hexagon', self.side))