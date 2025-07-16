Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/ADITI SHARMA/OneDrive/Desktop/calculator.py
>>> while True:
...     print("\nEnter 'exit' to quit.")
...     op = input("Choose operation (+, -, *, /): ")
...     
...     if op == "exit":
...         print("Exiting calculator. Goodbye!")
...         break
...     
...     if op not in ['+', '-', '*', '/']:
...         print("Invalid operation. Try again.")
...         continue
... 
...     try:
...         num1 = float(input("Enter first number: "))
...         num2 = float(input("Enter second number: "))
...     except ValueError:
...         print("Invalid input. Please enter numeric values.")
...         continue
... 
...     if op == '+':
...         result = add(num1, num2)
...     elif op == '-':
...         result = subtract(num1, num2)
...     elif op == '*':
...         result = multiply(num1, num2)
...     elif op == '/':
...         result = divide(num1, num2)
... 
...     print(f"Result: {result}")
... 
... 13-4
SyntaxError: invalid syntax
>>> 13-4
9
>>> 
>>> 5%6
5
>>> 6*58
348
