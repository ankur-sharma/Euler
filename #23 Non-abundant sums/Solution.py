import math
import array

def getProperDivisorSum(number):
    properDivisors = [1]

    sqrRoot = int(math.pow(number, 0.5)) + 1
    for i in range(2, sqrRoot, 1):
        if (number % i == 0):
            properDivisors.append(i)
            x = number // i
            if x not in properDivisors:
                properDivisors.append(x)

    return sum(properDivisors)


limit = 28123
abundantNumbers = array.array('i', [])
for number in range(1, limit, 1):
    divisorSum = getProperDivisorSum(number)
    if divisorSum > number:
        abundantNumbers.append(number)


numbersAsSumOfAbundantNumbers = {}
for i in range(0, len(abundantNumbers)-1, 1):
    for j in range(i, len(abundantNumbers)-1, 1):
        number = abundantNumbers[i] + abundantNumbers[j]
        if number <= limit:
            numbersAsSumOfAbundantNumbers[number] = True
        else:
            break
        
nonAbundantSum = 0
for number in range(1, limit, 1) :
    if number not in numbersAsSumOfAbundantNumbers.keys():
        nonAbundantSum+= number
        
print(nonAbundantSum)
            