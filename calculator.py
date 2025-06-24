from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon
from shape import InvalidDimensionError

# Shape creation functions - each function gets input from user and returns a shape object
def create_rectangle():
    w = float(input("Width: "))
    h = float(input("Height: "))
    return Rectangle(w, h)

def create_square():
    s = float(input("Side: "))
    return Square(s)

def create_triangle():
    b = float(input("Base: "))
    h = float(input("Height: "))
    return Triangle(b, h)

def create_circle():
    r = float(input("Radius: "))
    return Circle(r)

def create_hexagon():
    s = float(input("Side: "))
    return Hexagon(s)

# Helper functions for displaying shape information
def display_shape_info(shape):
    """Display the name, area and perimeter of a shape"""
    print(f"\nCreated: {shape.name}")
    print(f"Area: {shape.get_area():.2f}")
    print(f"Perimeter: {shape.get_perimeter():.2f}")

def list_shapes(shapes):
    """Display all shapes in the list with their index"""
    if not shapes:
        print("No shapes created yet.")
    for i, shape in enumerate(shapes, 1):
        print(f"{i}, {shape}")

def main():
    """Main program loop - handles user input and shape creation"""
    # List to store all created shapes
    shapes = [] 
    while True:
        # Display menu
        print("\nChoose a shape to create:")
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")
        print("5. Hexagon")
        print("6. List all shapes")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        try:
            # Process user's choice
            if choice == '1':
                shape = create_rectangle()
                shapes.append(shape)
                display_shape_info(shape)
            elif choice == '2':
                shape = create_square()
                shapes.append(shape)
                display_shape_info(shape)
            elif choice == '3':
                shape = create_triangle()
                shapes.append(shape)
                display_shape_info(shape)
            elif choice == '4':
                shape = create_circle()
                shapes.append(shape)
                display_shape_info(shape)
            elif choice == '5':
                shape = create_hexagon()
                shapes.append(shape)
                display_shape_info(shape)
            elif choice == '6':
                list_shapes(shapes)
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except InvalidDimensionError as e:
            # Handle shape creation errors
            print(f"Error: {e}")
        except ValueError:
            # Handle input conversion errors
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()