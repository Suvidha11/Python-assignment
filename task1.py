'''Task 1: Calculate Area with Conditions
Write a Python function calculate_area that takes two parameters: length and width. It
should calculate and return the area of a rectangle. However, add a condition: if the length
is equal to the width, return "This is a square!" instead of the area. Then, write a program to
input values for length and width from the user and call the calculate_area function to
display either the area or the message.'''


# function to calculate the area of a rectangle or determine if it's a square
def calculate_area(length,width):
    # Check if the length and width are equal,indicating a square
    if length==width:
        return  "This is a square! "   
    # If the length and width are different, calculate the area of a rectangle
    else:
        return length*width
    
# Get user input for the length and width of the rectangle
length=float(input("Enter the length:"))
width=float(input("Enter the width:"))

# Call the calculate_area function and store the result
result=calculate_area(length,width)
print(result)