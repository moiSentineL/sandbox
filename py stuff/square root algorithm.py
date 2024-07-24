import time

def expression(constant, assume):
    a = constant
    x_n0 = assume

    x_n = ((x_n0 + (a/x_n0))/2) 

    return x_n

def algorithm(c):
    x_n0 = 1

    while True:
        x_n = expression(c, x_n0)

        if x_n != x_n0:
            x_n0 = x_n
            print(x_n)
        else:
            print("aha here's your square root^^")
            break

        time.sleep(0.5)

if __name__ == "__main__":
    algorithm(10) # input stuff (the number)