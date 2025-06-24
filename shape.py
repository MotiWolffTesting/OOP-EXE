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
        
        
        def __str__(self):
            return f"{self.name}: Area={self.get_area():.2f}, Perimeter={self.get_perimeter():.2f}"

            

        
        
      
      