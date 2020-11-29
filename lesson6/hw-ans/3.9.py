import math

def main():
    n = int(input("n = "))
    maxima = -math.inf
    minima = math.inf
    s = 0
    for i in range(0, n):
        x = int(input("x{} = ".format(i)))
        if (x > maxima):
            maxima = x
        if (x < minima):
            minima = x
        s += x
    print("The sum is {}, The maxima is {}, The minima is {}".format(s, maxima, minima))


main()
