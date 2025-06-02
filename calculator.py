# create a basic calculator that can add, subtract, multiply, and divide two numbers

def add(x, y):
    """Return the sum of x and y."""
    return x + y
def subtract(x, y):
    """Return the difference of x and y."""
    return x - y
def multiply(x, y):
    """Return the product of x and y."""
    return x * y    
def divide(x, y):
    """Return the quotient of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def calculator():
    """A simple calculator function."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid input")
if __name__ == "__main__":
    calculator()
# This code defines a simple calculator that can perform addition, subtraction, multiplication, and division.
# It prompts the user to select an operation and input two numbers, then performs the selected operation and displays the result.
# The calculator function handles invalid inputs and division by zero gracefully.
# The code is structured to be run as a standalone script, allowing for easy testing and use.   
# The calculator function is the main entry point for the program, allowing users to interact with the calculator.
# The code is designed to be user-friendly, with clear prompts and error handling.
# The calculator supports basic arithmetic operations and handles division by zero errors.
# The code is modular, with separate functions for each arithmetic operation, making it easy to maintain and extend.
# The calculator can be easily extended to include more operations or features in the future.
# The code is written in Python, making it accessible to a wide range of users and developers.

# The calculator can be run directly from the command line or imported as a module in other Python scripts.
# The code is well-documented with docstrings, providing clarity on the purpose of each function.
# The calculator uses Python's built-in input and print functions for user interaction.
# The code is structured to handle user input and output in a straightforward manner.
# The calculator can be easily modified to include additional features, such as error logging or advanced mathematical functions.
# The code is designed to be simple and easy to understand, making it suitable for beginners learning Python.
# The calculator can be used in various applications, such as educational tools or simple arithmetic tasks.


