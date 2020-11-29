def main():
    done = False
    while (not done):
        for j in range(0, 3):
            x = int(input("x{} = ".format(j)))
            print(x)
        again = input("more? y/n?")
        if (again != "y"):
            done = True


main()
