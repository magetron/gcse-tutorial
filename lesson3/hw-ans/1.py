def readInput():
    s1 = input("Please input string1:")
    s2 = input("Please input string2:")
    return (s1, s2)

def stringCmpAndPrint(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if (len1 > len2):
        print(str1[len2 - 1])
    elif (len2 > len1):
        print(str2[len1 - 1])
    else: # len2 == len1
        print(str1[len1 - 1] + " " + str2[len2 - 1])

def main():
    (string1, string2) = readInput()
    stringCmpAndPrint(string1, string2)

main()
