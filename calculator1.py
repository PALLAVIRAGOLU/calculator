def addition(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def division(a, b):
    print(a / b)

def quotient(a, b):
    print(a // b)

def remainder(a, b):
    print(a % b)

def power(a, b):
    print(a ** b)

while True:
    n1 = input("Enter the first number (or type 'Exit' to end): ")
    
    if n1.lower() == 'exit':
        break

    n2 = input("Enter the second number: ")
    op = input("Enter the operation (+, -, *, /, //, %, ^): ")

    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    if op == '+':
        addition(n1, n2)
    elif op == '-':
        sub(n1, n2)
    elif op == '*':
        multiply(n1, n2)
    elif op == '/':
        division(n1, n2)
    elif op == '//':
        quotient(n1, n2)
    elif op == '%':
        remainder(n1, n2)
    elif op == '^':
        power(n1, n2)
    else:
        print("Enter a valid operation")
