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
        # Currently working only with isosceles triangles
        side = sqrt((self.width / 2) ** 2 + self.height ** 2)
        return self.width + 2 * side
    
    def __str__(self):
        return f"Triangle(base={self.width}, height={self.height}): Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"
    
    def __repr__(self):
        return f"Triangle(base={self.width}, height={self.height})"
    
    # Arithmetic operations
    def __mul__(self, factor):
        """Scale triangle by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Triangle(self.width * factor, self.height * factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __truediv__(self, factor):
        """Scale triangle by dividing dimensions by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return Triangle(self.width / factor, self.height / factor)
        else:
            raise ValueError("Scale factor must be a positive number")
    
    def __pow__(self, power):
        """Raise triangle's dimensions to a power"""
        if isinstance(power, (int, float)):
            return Triangle(self.width ** power, self.height ** power)
        return NotImplemented
    
    def __add__(self, other):
        """Add two triangles by adding their dimensions"""
        if isinstance(other, Triangle):
            return Triangle(self.width + other.width, self.height + other.height)
        return super().__add__(other)
    
    def __sub__(self, other):
        """Subtract two triangles by subtracting their dimensions"""
        if isinstance(other, Triangle):
            new_base = self.width - other.width
            new_height = self.height - other.height
            if new_base <= 0 or new_height <= 0:
                raise ValueError("Resulting dimensions would be non-positive")
            return Triangle(new_base, new_height)
        return super().__sub__(other)
    
    # Comparison methods specific to triangles
    def __eq__(self, other):
        if isinstance(other, Triangle):
            return self.width == other.width and self.height == other.height
        return super().__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, Triangle):
            return self.get_area() < other.get_area()
        return super().__lt__(other)
    
    # Hash method
    def __hash__(self):
        return hash(('Triangle', self.width, self.height))