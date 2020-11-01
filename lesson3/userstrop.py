def readInput():
    print("Operations:")
    print("1. convert to lowercase")
    print("2. convert to uppercase")
    print("3. convert to title case")
    print("4. convert to first letter capitalised")

    op = int(input("Please input an operation:"))
    s = input("Please input a string:")
    return (op, s)

def operateString(op, s):
    if (op == 1):
        return s.lower()
    elif (op == 2):
        return s.upper()
    elif (op == 3):
        return s.title()
    elif (op == 4):
        return s.capitalize()

def main():
    (op, s) = readInput()
    print(operateString(op, s))

main()
