import math

numberSumMap = {}


def getProperDivisorSum(number):
    properDivisors=[1]
        
    sqrRoot = int(math.pow(number, 0.5))+1
    for i in range(2, sqrRoot, 1):
        if (number%i==0):
            properDivisors.append(i)
            properDivisors.append(number//i)
            
    
    sum = 0
    for i in properDivisors:
        sum+=i
        
    return sum
    
for i in range(1, 10000, 1):
    sum = getProperDivisorSum(i)
    numberSumMap[i]=sum

# print(numberSumMap)    

sumOfAmicableNumber = 0
for a,b in numberSumMap.items():
    if a != b and b in numberSumMap and numberSumMap[b] == a:
        print(a,b)
        sumOfAmicableNumber+=a
        
print(sumOfAmicableNumber)