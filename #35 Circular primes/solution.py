import math

def isPrime(n):
    sqrt = int(math.sqrt(n))+1
    if n%2 == 0:
        return False
    for i in range(3, sqrt, 2):
        if n%i == 0:
            return False
    return True


def getCircularPrimeLen(n, primes):
    s = str(n)
    for i in range(len(s)):
        if s not in primes:
            return 0
        s = s[1:]+s[:1]
    return len(s)
        
    
numberOfCircularPrime = 0
primes = {}
for n in range(2, 1000000):
    if isPrime(n):
        primes[str(n)]=True
        numberOfCircularPrime += getCircularPrimeLen(n, primes)
            
print(numberOfCircularPrime)
            