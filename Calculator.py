# This is a simple calculator using functions

# Function to add two numbers
def add(a, b):
    return a + b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Ask user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user what operation they want
print("Choose operation:")
print("1. Add")
print("2. Multiply")

choice = input("Enter 1 or 2: ")

# Perform the chosen operation using the functions
if choice == '1':
    result = add(num1, num2)
    print("The sum is:", result)
elif choice == '2':
    result = multiply(num1, num2)
    print("The product is:", result)
else:
    print("Invalid choice. Please enter 1 or 2.")
