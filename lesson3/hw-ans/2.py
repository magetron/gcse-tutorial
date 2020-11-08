def readInput():
    index = int(input("Please input an index:"))
    string = input("Please input a string:")
    return (index, string)

def errorCheck(index, string):
    if (index < 0):
        print("ERROR! The index is not valid!")
        return False
    elif (index >= len(string)):
        print("ERROR! The string is not long enough!")
        return False
    else:
        return True

def prettyPrint(index, string):
    print("The character at index {} of \"{}\" is '{}'".format(index, string, string[index]))

def main():
    (i, s) = readInput()
    if (errorCheck(i, s)):
        prettyPrint(i, s)

main()
