def forloop():
    for i in reversed(range(1, 101)):
        print(i)


def whileloop():
    i = 100
    while (i >= 1):
        print(i)
        i -= 1


def main():
    forloop()
    whileloop()


main()
