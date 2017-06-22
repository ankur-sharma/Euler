import math


listOfPowers = {}


def getPowers(n):
    if n not in listOfPowers.keys():
        listOfPowers[n] = []
    return listOfPowers[n]


def getRoot(n):
    i = 2
    root = 1
    base = n
    while True:
        x = int(n**(1. / i))
        if x == 1:
            return root, base
        if x**i == n and i > root:
            root = i
            base = x
        i += 1


def brute(n):
    listN = []
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            x = i**j
            if x not in listN:
                listN.append(i**j)
    return len(listN)


n = 100

for i in range(2, n + 1):
    r, b = getRoot(i)
    powers = getPowers(b)
    for j in range(2, n + 1):
        x = r * j
        if x not in powers:
            powers.append(x)

distinctPower = 0
for key in listOfPowers.keys():
    distinctPower += len(listOfPowers[key])


print(distinctPower)
print(brute(n))
