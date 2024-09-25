# Write a Python program that takes two numbers as input and performs division, but handles the case where the denominator is zero by printing "Division by zero is not allowed."

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        

divide(10, 0)
