def readInput():
    str1 = input("Please input string 1:")
    str2 = input("Please input string 2:")
    return (str1, str2)

def isStringEqual(str1, str2):
    return str1 == str2

def prettyPrintResult(result):
    if (result):
        print("string 1 and 2 are the same")
    else:
        print("string 1 and 2 are different")

def main():
    (str1, str2) = readInput()
    result = isStringEqual(str1, str2)
    prettyPrintResult(result)


main()
