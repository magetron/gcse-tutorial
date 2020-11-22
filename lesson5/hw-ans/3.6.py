def readInput():
    num1 = int(input("Please input num1:"))
    num2 = int(input("Please input num2:"))
    return (num1, num2)

def forloop(num1, num2):
    for i in range(num1, num2 + 1):
        print(i)

def whileloop(num1, num2):
    i = num1
    while (i <= num2):
        print(i)
        i += 1

def main():
    (num1, num2) = readInput()
    forloop(num1, num2)
    whileloop(num1, num2)


main()
