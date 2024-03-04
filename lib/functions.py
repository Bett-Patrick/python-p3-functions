#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    pass
    print(f"Hello, {name}!")

greet("Patrick")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")

greet_with_default("Engineer Bett")

def add(num1, num2):
    pass
    num_sum = num1+num2
    print(num_sum)
    return num_sum

add(2,5)

def halve(number):
    pass
    output = number/2
    print(f"${output:.2f}")
    return output

halve(77)
