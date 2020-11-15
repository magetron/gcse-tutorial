def readInput():
    name = input("Please input the student's name:")
    mark1 = int(input("Please input the mark of exam paper1:"))
    mark2 = int(input("Please input the mark of exam paper2:"))
    courseWork1 = int(input("Please input the mark for coursework1:"))
    courseWork2 = int(input("Please input th mark for coursework2:"))
    return (name, mark1, mark2, courseWork1, courseWork2)

def calculation(mark1, mark2, courseWork1, courseWork2):
    totalMark = mark1 + mark2 + courseWork1 + courseWork2
    overallPercentage = totalMark / 250 * 100
    overallGrade = ""
    if (overallPercentage >= 80):
        overallGrade = "distinction"
    elif (65 <= overallPercentage) and (overallPercentage < 80):
        overallGrade = "merit"
    elif (50 <= overallPercentage) and (overallPercentage < 65):
        overallGrade = "pass"
    else:
        overallGrade = "fail"
    return (totalMark, overallPercentage, overallGrade)

def main():
    (name, mark1, mark2, courseWork1, courseWork2) = readInput()
    (tM, oP, oG) = calculation(mark1, mark2, courseWork1, courseWork2)
    print("The name of the student is {}, the total is {} and the overall percentage is {}%, the grade is {}.".format(name, tM, oP, oG))


main()
