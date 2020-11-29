def main():
    n = int(input("n = "))
    s = 0
    for i in range(0, n):
        x = int(input("x{} = ".format(i)))
        s += x
    print("The average is {}".format(s/x))


main()
