# Start of the program
while True:
    # Getting the first number with input validation
    while True:
        try:
            num1 = float(input("Enter the first number: "))  # Input the first number
            break  # If the input is valid, exit the loop
        except ValueError:
            print("Invalid input. Please enter a numeric value")  # If input is not a number, show an error message
    
    # Getting the operator with input validation
    while True:    
        try:
            operation = input("Enter the operator (+, -, *, /): ")  # Input the operator
            if operation in ("+", "-", "*", "/"):  # Ensure the operator is one of the valid choices
                break  # If the operator is valid, exit the loop
            else:
                raise ValueError  # If the operator is invalid, raise an error
        except ValueError:
            print("Invalid input. Please enter any of (+, -, /, *)")  # Show error message for invalid input
    
    # Getting the second number with input validation and handling division by zero
    while True:
        try:
            num2 = float(input("Enter the second number: "))  # Input the second number
            if num2 == 0 and operation == "/":  # Check if the operation is division by zero
                raise ZeroDivisionError  # Raise an error for division by zero
            break  # If the input is valid, exit the loop
        except ZeroDivisionError:
            print("Can't divide by zero, please enter another numeric value")  # Show error for division by zero
        except ValueError:
            print("Invalid input. Please enter a numeric value")  # Show error for invalid input

    # Perform the arithmetic operation based on the entered operator
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = None  # If an unexpected error occurs, set result to None

    # Display the result or show an error if result is None
    if result is not None:
        print("The Result is: ", result)
    else:
        print("Unexpected error!")  # Show error message for unexpected issues

    # Ask if the user wants to perform another operation
    while True:
        repeat = input("DO you want to perform another operation? (y/n): ").strip().lower()  # Input whether to repeat
        if repeat == "y":
            break  # If yes, restart the program
        elif repeat == "n":
            print("Program exited")  # If no, exit the program
            exit()  # Exit the program
        else:
            print("Invalid input, please choose between (y/n)")  # Show error for invalid input
