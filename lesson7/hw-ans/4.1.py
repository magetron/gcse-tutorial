
def main():
    done = False
    s = 0
    i = 0
    while (not done):
        x = int(input("Please input a number:"))
        hasNext = input("Continue(y/n)?")
        if (hasNext != 'y'):
            done = True

        s += x
        i += 1

    print("The avg. is {}".format(s / i))


main()
