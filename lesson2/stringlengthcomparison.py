def readInput():
    str1 = input("Please input string 1:")
    str2 = input("Please input string 2:")
    return (str1, str2)

def isFirstLonger(str1, str2):
    if len(str1) > len(str2):
        return 1
    elif len(str1) == len(str2):
        return 0
    else:
        return -1

def prettyPrintResult(result):
    if (result == 1):
        print("string 1 is longer than string 2")
    elif (result == 0):
        print("string 1 and 2 are of the same length")
    else:
        print("string 2 is longer than string 1")

def main():
    (str1, str2) = readInput()
    result = isFirstLonger(str1, str2) # result = 1 or 0 or -1
    prettyPrintResult(result)

main()

