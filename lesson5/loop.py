def main():
    for i in range(1, 101):
        print(i)

    i = 0
    while (i <= 100):
        print(i)
        i += 10

    for i in reversed(range(1, 101)):
        print(i)

    print([x for x in range(100, 0, -1)])

    i = 100
    while (i >= 0):
        print(i)
        i -= 1

    for i in range(5)[::-1]:
        print(i)

main()
