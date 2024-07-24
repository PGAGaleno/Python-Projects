calculator = input("Please choose an operation!")
num1 = float(input("Please enter a number! "))
num2 = float(input("Please enter a number! "))

if calculator == "+":
    result = num1 + num2
    print(round(result, 3))
elif calculator == "-":
    result = num1 - num2
    print(round(result, 3))
elif calculator == "*":
    result = num1 * num2
    print(round(result, 3))
elif calculator == "/":
    result = num1 / num2
    print(round(result, 3))