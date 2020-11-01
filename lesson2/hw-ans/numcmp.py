def readInput():
    num1 = int(input("Please input number 1:"))
    num2 = int(input("Please input number 2:"))
    return (num1, num2)

def numCmp(num1, num2):
    if (num1 > num2):
        return 1
    elif (num1 == num2):
        return 0
    else:
        return -1

def prettyPrintResult(result, num1, num2):
    if (result == 1):
        print("{} > {}".format(num1, num2)) # num1 > num2
    elif (result == 0):
        print("{} = {}".format(num1, num2)) # num1 = num2
    else:
        print("{} < {}".format(num1, num2)) # num1 < num2

def main():
    (num1, num2) = readInput()
    result = numCmp(num1, num2)
    prettyPrintResult(result, num1, num2)


main()
