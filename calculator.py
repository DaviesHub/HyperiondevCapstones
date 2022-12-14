# A simple calculator program that performs arithmetic operations on two numbers


# Define calculator function to be called when user opts for the calculator
def calculator():
    """This function is a simple simulation of a binary operations calculator"""

    # Prompt input for both numbers
    while True:
        num_one = input("Enter the first number: ")
        num_two = input("Enter the second number: ")

        try:
            if "." in num_one: # If one of the numbers has a point, it is considered to be a float. Otherwise, it is treated as an integer
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

    # Prompt user for artithmetic operation
    while True:
        operation = input('''Enter the operation you'd like to perform on both numbers:
    # Enter + for addition
    # Enter - for subtraction
    # Enter * for multiplication
    # Enter / for division
    # : ''')

        if operation == "+":
            result = num_one + num_two
            # When one of the operands is a float, result is a decimal and is rounded to 2 decimal places
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


print("\n=== This calculator performs arithmetic operations on two numbers===")
while True:
    menu = input('''\nMenu:
===> Enter 1 to use calculator
===> Enter 2 to view equations
===> Enter 3 to exit
===>: ''')
    if menu == "1":
        calculator()

    elif menu == "2":
        while True:
            filename = input("\nEnter the name of the txt file to read equations from: ")
            try:
                fhand = open(filename, 'r')
                content = fhand.read()
                print(content)
                fhand.close()
                break
            except FileNotFoundError:
                print("The file does not exist")             

    elif menu == "3":
        exit()

    else:
        print("Invalid option.")