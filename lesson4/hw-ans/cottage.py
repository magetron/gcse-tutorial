def readInput():
    duration = int(input("Please input a duration:"))
    month = input("Please input the month of the stay:")
    swimming_pool = (input("With Swimming Pool? (y/n) ") == "y")
    playground = (input("With Children's Playground? (y/n) ") == "y")
    tennis_court = (input("With Tennis Court? (y/n) ") == "y")
    mini_golf = (input("With Mini Golf? (y/n) ") == "y")
    hot_tub = (input("With Hot Tub? (y/n) ") == "y")
    return (duration, month, swimming_pool, playground, tennis_court, mini_golf, hot_tub)

def calc(d, m, sp, p, tc, mg, ht):
    cost = 0
    # Cottage Cost
    if (m == "June" or m == "July" or m == "August"):
        cost += 120 * d
    else:
        cost += 90 * d

    if (sp):
        cost += 50
    if (p):
        cost += 25
    if (tc):
        cost += 45
    if (mg):
        cost += 15
    if (ht):
        cost += 50

    return cost


def main():
    (d, m, sp, p, tc, mg, ht) = readInput()
    #print("{} {} {} {} {} {} {}".format(d, m, sp, p, tc, mg, ht))
    cost = calc(d, m, sp, p, tc, mg, ht)
    print("The cost of the cottage is {}.".format(cost))

main()
