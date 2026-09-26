"""
Simple Calculator
CodeOrbit Tech - Python Programming Internship (Task 1)

Performs basic arithmetic operations (add, subtract, multiply, divide)
based on user input, with error handling for invalid input and
division by zero.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """
    Keep asking the user for input until a valid float is entered.
    This protects the rest of the program from crashing on bad input.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g. 5 or 3.2).")


def get_operation():
    """Ask the user to choose an operation and validate the choice."""
    valid_ops = {"1": "+", "2": "-", "3": "*", "4": "/"}
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice in valid_ops:
            return valid_ops[choice]
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


def calculate(num1, operation, num2):
    """Perform the calculation based on the chosen operation."""
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)


def main():
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        # Get two numbers and the chosen operation from the user
        num1 = get_number("Enter the first number: ")
        operation = get_operation()
        num2 = get_number("Enter the second number: ")

        try:
            result = calculate(num1, operation, num2)
            print(f"\nResult: {num1} {operation} {num2} = {result}\n")
        except ZeroDivisionError as e:
            # Handle division by zero gracefully instead of crashing
            print(f"\nError: {e}\n")

        # Ask if the user wants to perform another calculation
        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
