def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("=== Simple Calculator ===")

while True:
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("q. Quit")

    choice = input("Choose an operation (1/2/3/4) or 'q' to quit: ")

    if choice.lower() == 'q':
        print("Goodbye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select a valid operation.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        continue

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {result:.2f}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {result:.2f}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {result:.2f}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = divide(num1, num2)
            print(f"Result: {result:.2f}")
