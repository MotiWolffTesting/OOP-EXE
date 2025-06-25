from abc import ABC, abstractmethod

class InvalidDimensionError(Exception):
    pass

class Shape(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_perimeter(self):
        pass
    
    # String representation
    def __str__(self):
        return f"{self.name}: Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"
    
    # Representation for debugging
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"
    
    # Comparison operators based on area
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.get_area() == other.get_area()
        return False
    
    # Less than operator
    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.get_area() < other.get_area()
        return NotImplemented
    
    # Less than or equal to operator
    def __le__(self, other):
        if isinstance(other, Shape):
            return self.get_area() <= other.get_area()
        return NotImplemented
    
    # Greater than operator
    def __gt__(self, other):
        if isinstance(other, Shape):
            return self.get_area() > other.get_area()
        return NotImplemented
    
    # Greater than or equal to operator
    def __ge__(self, other):
        if isinstance(other, Shape):
            return self.get_area() >= other.get_area()
        return NotImplemented
    
    # Inequality operator
    def __ne__(self, other):
        return not self.__eq__(other)
    # End of comparison operators
    
    # Hash method for using shapes in sets/dicts
    def __hash__(self):
        return hash((self.name, round(self.get_area(), 2), round(self.get_perimeter(), 2)))
    
    # Arithmetic operations
    # Addition operator
    def __add__(self, other):
        """Add areas of two shapes"""
        if isinstance(other, Shape):
            return self.get_area() + other.get_area()
        return NotImplemented
    
    # Subtraction operator
    def __sub__(self, other):
        """Subtract areas of two shapes"""
        if isinstance(other, Shape):
            return self.get_area() - other.get_area()
        return NotImplemented
    
    # Multiplication operator
    def __mul__(self, factor):
        """Scale shape by a factor (to be implemented by subclasses)"""
        return NotImplemented
    
    # Division operator
    def __truediv__(self, factor):
        """Scale shape by dividing dimensions by a factor"""
        if isinstance(factor, (int, float)) and factor > 0:
            return self.__mul__(1 / factor)
        return NotImplemented
    
    # Context manager support
    def __enter__(self):
        return self
    
    # Context manager exit method
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

            

        
        
      
      