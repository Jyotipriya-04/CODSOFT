import math
#making a simple calculator using different operator such as addition, subtraction,division,multiplication, power and square root
print("Select an operation to perform: ( 1 - 6 )")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")


operation = int(input())

if operation == 1:#perfoming addition
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print("The sum is ", + num1 + num2)

elif operation == 2:#performing subtraction
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print("The difference is ", + num1- num2)

elif operation == 3:#performing multiplication
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    print("The product is ", + num1 * num2)

elif operation == 4:#performing division
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    if num2!=0:
        print("The result is ", + num1 / num2)
    else:
        print("cannot be divided by zero.")

elif operation == 5:#performing squareroot
    num = int(input("Enter number:"))
    print("The squareroot is %f " %(math.sqrt(num)))#float is used for decimal value


elif operation == 6:#performing power
     num = int(input("Enter the  number:"))
     power=int(input("Enter the power:"))
     print("The result is " ,pow(num, power))

else:
    print("Invalid operation.")





