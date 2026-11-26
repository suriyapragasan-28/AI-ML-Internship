print("===== SIMPLE CALCULATOR =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

operator = input("Enter your operator: ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operator!")
