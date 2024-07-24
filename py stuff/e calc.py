from sympy import * # This package allows you to do complex mathematical equations

iteration = 0 # where x = iterations
while True:
    iteration += 1000

    x = symbols("x")
    expression = (1+1/x)**x # (1+1/x)^x

    form = limit(expression, x, iteration)

    print(f"When x = {iteration} -> {float(form)}")
