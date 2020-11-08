def readInput():
    depth = int(input("Depth:"))
    length = int(input("Length:"))
    width = int(input("Width:"))
    return (depth, length, width)

def calcStats(depth, length, width):
    volume = 0.75 * depth * length * width
    topup_cost = volume * 0.02 * 0.5
    clean_cost = volume / 100 * 1.2
    heating_cost = volume / 100 * 3.0
    total_cost = topup_cost + clean_cost + heating_cost
    return (volume, topup_cost, clean_cost, heating_cost, total_cost)

def prettyPrint(volume, topup_cost, clean_cost, heating_cost, total_cost):
    print("The volume of water in the pool is {:.2f}".format(volume))
    print("The cost of water 'top up' per day is {:.2f}".format(topup_cost))
    print("The cost of water cleaning per day is {:.2f}".format(clean_cost))
    print("The cost of water heating per day is {:.2f}".format(heating_cost))
    print("The total cost of running the pool per day is {:.2f}".format(total_cost))
    print("The total cost of running the pool per week is {:.2f}".format(total_cost * 7))
    print("The total cost of running the pool per year is {:.2f}".format(total_cost * 365))

def main():
    (d, l, w) = readInput()
    prettyPrint(*calcStats(d, l, w))

main()
