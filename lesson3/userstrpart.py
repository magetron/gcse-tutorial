def readInput():
    index = int(input("Please input an index:"))
    s = input("Please input a string:")
    return (index, s)

def prettyPrint(index, s):
    print("The character at index {} of \"{}\" is '{}'".format(index, s, s[index]))
    #     " The character at index {} of \"{}\" is    '{}' "
    # format                      index    s          s[index]
    #                              6     Hello World   W
    #       The character at index 6 of "Hello World" is 'W'

def main():
    (index, s) = readInput()
    prettyPrint(index, s)

main()
