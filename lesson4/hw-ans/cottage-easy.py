d = int(input("Please input a duration:"))
m = input("Please input the month of the stay:")
sp = (input("With Swimming Pool? (y/n) ") == "y")
p = (input("With Children's Playground? (y/n) ") == "y")
tc = (input("With Tennis Court? (y/n) ") == "y")
mg = (input("With Mini Golf? (y/n) ") == "y")
ht = (input("With Hot Tub? (y/n) ") == "y")

cost = 0
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

print("The cost of the cottage is {}.".format(cost))

