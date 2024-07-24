import time
import sys

def expression(constant, assume):
    a = float(constant)
    x_n0 = float(assume)

    x_n = ((x_n0 + (a/x_n0))/2) 

    return x_n

def algorithm(c):
    x_n0 = 1

    while True:
        x_n = expression(c, x_n0)

        if x_n != x_n0:
            x_n0 = x_n
            print(x_n)
        elif x_n == 1:
            print("fuck youuu")
        else:
            print("aha here's your square root^^")
            break

        time.sleep(0.5)

if __name__ == "__main__":
    if isinstance(sys.argv[0], str):
        try:
            arg = sys.argv[1]
            algorithm(arg) # input stuff (the number)
        except IndexError as e:
            print("bruh type a number")
    else:
        arg = sys.argv[0]
        algorithm(arg) # input stuff (the number)
    