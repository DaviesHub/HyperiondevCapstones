# Code to compute the highest common factor of two integers
print("\nEnter any 2 positive integers")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

while True:
    if num1 <= 0 or num2 <= 0:
        print("\nYou have entered a negative number. Enter 2 positive integers")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        continue
    elif num1 == num2:
        hcf = num1 # HCF of the same numbers is the number
        print("The highest common factor of {} and {} is {}".format(num1, num1, hcf))
    elif num1 == 1 or num2 == 1:
        hcf = 1 # HCF of 1 and a positive number is 1
        print("The highest common factor of {} and {} is {}".format(num1, num1, hcf))
    else:
        if num1 < num2: # Find the smallest number
            min_num = num1
        else:
            min_num = num2
        
        for i in range(1, min_num + 1):