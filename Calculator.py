while True:
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except  ValueError:
            print("Invalid input. Please enter a numeric value")
    while True:    
        try:
            operation = input("Enter the operator (+, -, *, /): ")
            if operation in ("+", "-", "*", "/"):
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter any of (+, -, /, *)")
        
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            if num2 == 0 and operation =="/":
                raise ZeroDivisionError
            break
        except ZeroDivisionError:
            print("Can't divide by zero, please enter another numeric value")
        except ValueError:
            print("Invalid input. Please enter a numeric value")


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = None

    if result != None:
        print("The Result is: ", result)
    else:
        print("Unexpected error!")

    while True:
        repeat = input("DO you want to perform another operation? (y/n): ").strip().lower()
        if repeat =="y":
            break
        elif repeat == "n":
            print("program exited")
            exit()
        else:
            print("Invalid input, please choose between (y/n)")
