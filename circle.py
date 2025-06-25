from shape import Shape, InvalidDimensionError
from math import pi

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidDimensionError("Radius must be a positive number!")
        super().__init__("Circle")
        self.radius = radius
        
        
    def get_area(self):
        return pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * pi * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"
    
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    # Arithmetic operations
    def __mul__(self, factor):
        """Scale circle by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Circle(self.radius * factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __truediv__(self, factor):
        """Scale circle by dividing radius by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Circle(self.radius / factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __pow__(self, power):
        """Raise circle's radius to a power"""
        if isinstance(power, (int, float)):
            return Circle(self.radius ** power)
        return NotImplemented
    
    def __add__(self, other):
        """Add two circles by adding their radii"""
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return super().__add__(other)
    
    def __sub__(self, other):
        """Subtract two circles by subtracting their radii"""
        if isinstance(other, Circle):
            new_radius = self.radius - other.radius
            if new_radius <= 0:
                raise ValueError("Resulting radius would be non-positive")
            return Circle(new_radius)
        return super().__sub__(other)
    
    # Comparison methods specific to circles
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return super().__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return super().__lt__(other)
    
    # Hash method
    def __hash__(self):
        return hash(('Circle', self.radius))
