

def coinSum(denominations, ammount):
    if ammount == 0 or len(denominations) == 0:
        return 0
    coinsum = 0
    i = denominations[0]
    if i > ammount:
        return coinSum(denominations[1:], ammount)
    else:
        a = ammount // i
        for j in range(a, -1, -1):
            if ammount == i*j:
                coinsum += 1
            else:
                coinsum += coinSum(denominations[1:], ammount - (i*j))

    return coinsum
        

print("Answer is ", coinSum((200, 100, 50, 20, 10, 5, 2, 1), 200))