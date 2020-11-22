def main():
    x = int(input("Please input x:"))
    y = int(input("Please input y:"))
    original_x = x
    ans = 0
    while (x >= y):
        print("{}: {} - {} = {}".format(ans, x, y, x - y))
        x -= y
        ans += 1
    print("{} divided by {} is {} remainder {}.".format(original_x, y, ans, x))


main()
