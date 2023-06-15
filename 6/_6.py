import math
import random
print("Enter an operation('+', '-', '*', '/', '**', 'mod', 'rand', 'fact', 'acos'):")
operation = input()

if operation == '+':
    print("Enter the first number:") 
    num1 = float(input())
    print("Enter the second number:") 
    num2 = float(input())
    print("Result:", num1 + num2) 

elif operation == '-':
    print("Enter the first number:") 
    num1 = float(input())
    print("Enter the second number:")
    num2 = float(input())
    print("Result:", num1 - num2)

elif operation == '*':
    print("Enter the first number:") 
    num1 = float(input())
    print("Enter the second number:") 
    num2 = float(input())
    print("Result:", num1 * num2) 

elif operation == '/':
    print("Enter the first number:") 
    num1 = float(input())
    print("Enter the second number:") 
    num2 = float(input())
    if num2 != 0:
        print("Result:", num1 / num2) 
    else:
        print("Division by 0 is impossible!") 

elif operation == '**':
    print("Enter the number to be raised to the power:") 
    num1 = float(input())
    print("Enter the power to which you want to raise the number:") 
    num2 = float(input())
    print("Result:", num1 ** num2) 

elif operation == 'mod':
    print("Enter the number:") 
    num1 = float(input())
    print("Enter module:") 
    num2 = float(input())
    print("Result:", num1 % num2) 

elif operation == 'rand':
    print("Enter a range to generate a random number:") 
    print("Enter the minimum number:") 
    num1 = int(input())
    print("Enter the maximum number:") 
    num2 = int(input())
    print("Random number from range [", num1, ",", num2, "]:", random.randint(num1, num2)) 

elif operation == 'fact':
    print("Enter a number to calculate the factorial:") 
    num1 = int(input())
    print("Result:", math.factorial(num1))

elif operation == 'acos':
    print("Enter a number to calculate the arc cosine (of -1 to 1):") 
    num1 = float(input())
    if -1 <= num1 <= 1:
        print("Result:", math.acos(num1)) 
    else:
        print("The number must be in the range of -1 to 1!")
