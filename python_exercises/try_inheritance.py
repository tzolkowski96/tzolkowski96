# Define a Shape class that prints a message indicating that it is a shape
class Shape: 
    def what_am_i(self): 
        print("I am a shape.") 

# Define a Rectangle class that inherits from the Shape class
class Rectangle(Shape):
    def __init__(self, width, length): 
        self.width = width 
        self.length = length 
    
    # Define a method that calculates the perimeter of the rectangle
    def calculate_perimeter(self): 
        return 2 * (self.width + self.length) 
    
# Define a Square class that inherits from the Shape class
class Square(Shape): 
    def __init__(self, s1): 
        self.s1 = s1 
    
    # Define a method that calculates the perimeter of the square
    def calculate_perimeter(self): 
        return 4 * self.s1 
    
    # Define a method that changes the size of the square by a given delta
    def change_size(self, delta): 
        self.s1 += delta 
 
# Create instances of the Rectangle and Square classes
rectangle = Rectangle(10, 20)
square = Square(10) 
 
# Call the what_am_i method on the instances of the Rectangle and Square classes
rectangle.what_am_i() 
square.what_am_i() 