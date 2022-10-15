# A simple calculator program that performs binary operations on two numbers

while True:
    print("\n=== This calculator performs arithmetic operations on two numbers===\n")
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

fhand = open("equations.txt", "a")
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
    
    elif operation == "-":
        result = num_one - num_two

    elif operation == "*":
        result = num_one * num_two
    
    elif operation == "/":
        result = num_one / num_two


fhand.write(f"{num_one} {operation} {num_two} = {result}\n")