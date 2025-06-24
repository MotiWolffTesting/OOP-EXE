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
        
        @abstractmethod
        def display_info(self):
            pass

        
        
      
      