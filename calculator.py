# A simple calculator program that performs arithmetic operations on two numbers


def calculator():
    """This function is a simple simulation of a binary operations calculator"""

    while True:
        num_one = input("Enter the first number: ")
        num_two = input("Enter the second number: ")

        try:
            if "." in num_one:
                num_one = float(num_one)
            else:
                num_one = int(num_one)

            if "." in num_two:
                num_two = float(num_two)
                break
            else:
                num_two = int(num_two)
                break

        except ValueError:
            print("Unsupported operand. Both operands must be numbers. Try again.")

    result = 0

    while True:
        operation = input('''Enter the operation you'd like to perform on both numbers:
    # Enter + for addition
    # Enter - for subtraction
    # Enter * for multiplication
    # Enter / for division
    # : ''')

        if operation == "+":
            result = num_one + num_two
            if isinstance(num_one, float) or isinstance(num_two, float):
                result = round(result, 2)
            break
    
        elif operation == "-":
            result = num_one - num_two
            if isinstance(num_one, float) or isinstance(num_two, float):
                result = round(result, 2)
            break

        elif operation == "*":
            result = num_one * num_two
            if isinstance(num_one, float) or isinstance(num_two, float):
                result = round(result, 2)
            break

        elif operation == "/":
            if num_two == 0: # Prevent division by zero
                result = "inf"
                print("Cannot perform division by zero")
                break

            result = num_one / num_two
            if isinstance(num_one, float) or isinstance(num_two, float):
                result = round(result, 2)
                break

        else:
            print("Invalid operand")

    print(result)
    fhand = open("equations.txt", "a")
    fhand.write(f"{num_one} {operation} {num_two} = {result}\n")
    fhand.close()


def view_equations(file):




print("\n=== This calculator performs arithmetic operations on two numbers===\n")
while True:
    menu = input('''\nMenu:
===> Enter 1 to use calculator
===> Enter 2 to view equations
===> Enter 3 to exit
===>: ''')
    if menu == "1":
        calculator()

    elif menu == "2":
        view_equations()

    elif menu == "3":
        exit()

    else:
        print("Invalid option.")











