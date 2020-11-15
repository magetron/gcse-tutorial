def readInput():
    weight = int(input("please input the weight of the parcel in grammes:"))
    class_post = int(input("whether First class or Second class post is required:"))
    insuranceWanted = input("do you want insurance, y or n:")
    itemWorth = 0
    if insuranceWanted == "y":
        itemWorth = int(input("please input the worth:"))
    return (weight, class_post, insuranceWanted, itemWorth)

def calcResult(weight, class_post, insuranceWanted, itemWorth):
    if class_post == 1:
        cost = 0.75 * (weight / 100) + 1.5
    else:
        cost = 0.55 * (weight / 100) + 1
    if insuranceWanted:
        if itemWorth > 25:
            cost += 5
        else:
            cost += 2
    return cost

def printResult(cost):
    print("The cost is {}.".format(cost))

def main():
    printResult(calcResult(*readInput()))


main()

