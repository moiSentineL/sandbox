from sympy import * # This package allows you to do complex mathematical equations

x = symbols("x")
iteration = 0 # where x = iterations
while True:
    iteration += 1000
    print(f"When x = {iteration} -> {float(limit((1+1/x)**x, x, iteration))}")
