PI = 3.141592653589

def getCircleArea(r):
    return PI * (r ** 2)


def main():
    r = float(input("radius=")) # input

    area = getCircleArea(r) # process

    print("The area of a circle with radius {} is {}.".format(r, area)) # output


main()



