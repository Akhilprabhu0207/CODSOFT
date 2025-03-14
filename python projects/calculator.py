def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error"
    else:
        return x / y


def main():
    print("Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    
    choice = input("Enter operation choice (1/2/3/4): ")

    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = None
    
    if choice == '1':
        result = add(num1,num2)
    elif choice == '2':
        result = subtract(num1,num2)
    elif choice == '3':
        result = multiply(num1,num2)
    elif choice == '4':
        result = divide(num1,num2)

    
    if isinstance(result,str):
        print(result)
    else:
        print(f"Result:{result}")

if __name__ == "__main__":
    main()
