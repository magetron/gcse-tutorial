def main():
    n1 = int(input("n1 = "))
    n2 = int(input("n2 = "))

    s = 0
    for i in range(n1, n2 + 1):
        s += i
    print(s)

    print( (n1 + n2) * (n2 - n1 + 1) / 2 )

main()
