def readInput():
    weight = int(input("Weight:"))
    class_post = int(input("Class of Post:"))
    insurance_required = input("insurance? y/n:")
    item_worth = 0
    if (insurance_required == "y"):
        item_worth = int(input("worth:"))
    return (weight, class_post, insurance_required, item_worth)

def checkStats(weight, class_post, insurance_required, item_worth):
    cost = 0
    if (class_post == 1):
        cost += 1.5
        cost += 0.75 * weight / 100
    elif (class_post == 2):
        cost += 1.0
        cost += 0.55 * weight / 100
    else:
        print("ERROR! class of post not valid.")
        return (False, 0)

    if (insurance_required == "n"):
        return (True, cost)
    elif (insurance_required == "y"):
        if (item_worth > 25):
            cost += 5
        elif (item_worth >= 0):
            cost += 2
        else:
            print("ERROR! item_worth < 0 not valid.")
            return (False, 0)
        return (True, cost)
    else:
        print("ERROR! insurance status unclear.")
        return (False, 0)

def main():
    (is_valid, cost) = checkStats(*readInput())
    if (is_valid):
        print("Total Cost = {}".format(cost))

main()


