from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from hexagon import Hexagon

def demo_comparison_operators():
    """Mimic comparison operators"""
    print("=== Comparison Operators ===")
    
    # Create shapes with different areas
    circle1 = Circle(3)
    circle2 = Circle(5)
    rectangle = Rectangle(4, 6)
    square = Square(4)
    
    print(f"Circle1 area: {circle1.get_area():.2f}")
    print(f"Circle2 area: {circle2.get_area():.2f}")
    print(f"Rectangle area: {rectangle.get_area():.2f}")
    print(f"Square area: {square.get_area():.2f}")
    
    print(f"\ncircle1 < circle2: {circle1 < circle2}")
    print(f"circle1 > circle2: {circle1 > circle2}")
    print(f"circle1 == circle2: {circle1 == circle2}")
    print(f"rectangle <= square: {rectangle <= square}")
    print(f"rectangle >= square: {rectangle >= square}")
    print(f"rectangle != square: {rectangle != square}")

def demo_arithmetic_operators():
    """Mimic arithmetic operators"""
    print("\n=== Arithmetic Operators ===")
    
    # Scaling operations
    circle = Circle(3)
    rectangle = Rectangle(4, 6)
    square = Square(5)
    
    print("Scaling operations:")
    print(f"Original circle: {circle}")
    scaled_circle = circle * 2
    print(f"Circle * 2: {scaled_circle}")
    divided_circle = circle / 2
    print(f"Circle / 2: {divided_circle}")
    
    print(f"\nOriginal rectangle: {rectangle}")
    scaled_rect = rectangle * 1.5
    print(f"Rectangle * 1.5: {scaled_rect}")
    
    print(f"\nOriginal square: {square}")
    powered_square = square ** 2
    print(f"Square ** 2: {powered_square}")
    
    # Addition and subtraction
    print("\nAddition and subtraction:")
    circle1 = Circle(2)
    circle2 = Circle(3)
    combined_circle = circle1 + circle2
    print(f"Circle(2) + Circle(3) = {combined_circle}")
    
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(1, 2)
    combined_rect = rect1 + rect2
    print(f"Rectangle(3,4) + Rectangle(1,2) = {combined_rect}")
    
    # Area arithmetic (from base class)
    print("\nArea arithmetic:")
    total_area = circle1 + rectangle  # Adds areas
    print(f"Circle area + Rectangle area = {total_area:.2f}")

def demo_hash_and_containers():
    """Mimic hash method and container usage"""
    print("\n=== Hash and Containers ===")
    
    # Create a set of shapes
    shapes_set = set()
    shapes_set.add(Circle(3))
    shapes_set.add(Circle(3))  # Duplicate
    shapes_set.add(Circle(4))
    shapes_set.add(Rectangle(2, 3))
    shapes_set.add(Square(4))
    
    print(f"Set of shapes (duplicates removed): {len(shapes_set)} shapes")
    for shape in shapes_set:
        print(f"  {shape}")
    
    # Create a dictionary
    shapes_dict = {
        Circle(3): "Small circle",
        Rectangle(4, 5): "Medium rectangle",
        Square(6): "Large square"
    }
    
    print(f"\nDictionary with shapes as keys:")
    for shape, description in shapes_dict.items():
        print(f"  {shape} -> {description}")

def demo_context_manager():
    """Mimic context manager support"""
    print("\n=== Context Manager ===")
    
    with Circle(5) as circle:
        print(f"Working with circle in context: {circle}")
        print(f"Area: {circle.get_area():.2f}")
    print("Context exited")

def demo_repr_and_str():
    """Mimic __repr__ and __str__ methods"""
    print("\n=== String Representations ===")
    
    circle = Circle(3)
    rectangle = Rectangle(4, 6)
    square = Square(5)
    triangle = Triangle(3, 4)
    hexagon = Hexagon(2)
    
    shapes = [circle, rectangle, square, triangle, hexagon]
    
    print("String representation (__str__):")
    for shape in shapes:
        print(f"  {shape}")
    
    print("\nRepr representation (__repr__):")
    for shape in shapes:
        print(f"  {repr(shape)}")

def demo_error_handling():
    """Mimic error handling in dunder methods"""
    print("\n=== Error Handling ===")
    
    try:
        circle = Circle(3)
        invalid_scale = circle * -1
    except ValueError as e:
        print(f"Error scaling by negative factor: {e}")
    
    try:
        circle1 = Circle(2)
        circle2 = Circle(5)
        result = circle1 - circle2  # Would result in negative radius
    except ValueError as e:
        print(f"Error subtracting larger circle: {e}")
    
    try:
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(4, 5)
        result = rect1 - rect2  # Would result in negative dimensions
    except ValueError as e:
        print(f"Error subtracting larger rectangle: {e}")

def main():
    """Run all mimics"""
    print("DUNDER METHODS MIMIC")
    print("=" * 50)
    
    demo_comparison_operators()
    demo_arithmetic_operators()
    demo_hash_and_containers()
    demo_context_manager()
    demo_repr_and_str()
    demo_error_handling()
    
    print("\n" + "=" * 50)
    print("Mimic complete!")

if __name__ == "__main__":
    main() 