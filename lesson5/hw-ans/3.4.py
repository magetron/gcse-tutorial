def forloop():
    n = int(input("Please input a number:"))
    for i in range(0, n + 1):
        print(i)

def whileloop():
    n = int(input("Please input a number:"))
    i = 0
    while (i <= n):
        print(i)
        i += 1

def main():
    forloop()
	whileloop()


main()
