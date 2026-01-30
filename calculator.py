num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Choose operation")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

op = input("Enter operator: ")

if op == "+":
    print("Result =", num1 + num2)

elif op == "-":
    print("Result =", num1 - num2)

elif op == "*":
    print("Result =", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")
