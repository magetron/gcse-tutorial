def readInput():
    grade = int(input("Please input a grade:"))
    return grade

def printGrade(grade):
    if (grade >= 70):
        print("1")
    elif (grade >= 65):
        print("2:1")
    elif (grade >= 60):
        print("2:2")
    elif (grade >= 50):
        print("3")
    elif (grade >= 40):
        print("pass")
    else:
        print("fail")

def main():
    #printGrade(readInput())
    g = readInput()
    printGrade(g)

main()
