
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("Welcome to the calc (slang for calculator).")

# Get numbers from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

op = input("What do you want to do? (+, -, *, /): ")

if op == "+":
    result = add(num1, num2)
    print(f"Fine. The sum is {result}. Are we done now?")

elif op == "-":
    result = subtract(num1, num2)
    print(f"Okay. The difference is {result}. Thrilling.")

elif op == "*":
    result = multiply(num1, num2)
    print(f"Great. The product is {result}. Try not to get too excited.")

elif op == "/":
    if num2 == 0:
        print("Wow. Divide by zero. You're a real genius. That's impossible.")
    else:
        result = divide(num1, num2)
        print(f"Sure. The quotient is {result}. Can I go back to sleep now?")

else:
    print("Error")
