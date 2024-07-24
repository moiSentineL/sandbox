import math

try:
    radius = int(input("Radius? "))
    Area = radius * radius * 3.14
    print (f"Area: {Area} sq. unit")
except ValueError:
    print("Make sure it's a number...")