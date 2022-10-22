from math import *
num1 = float(input("first number"))
operation = (input("choose an operation")).lower()
num2 = float(input("second number"))

def math():
    if operation == "add" or operation == "plus":
        print(num1 + num2)
    if operation == "minus" or operation == "take away":
        print(num1 - num2)
    if operation == "multiply" or operation == "times":
        print(num1 * num2)
    if operation == "divide" or operation == "into groups off":
        print(num1 / num2)

math()