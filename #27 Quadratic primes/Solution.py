import math


def isPrime(number):
    if number <= 0:
        return False
    if number % 2 == 0:
        return number == 2
    sqrRoot = int(math.sqrt(number))
    for i in range(3, sqrRoot + 1, 2):
        if number % i == 0:
            return False
    return True


def primeFunction(n, a, b):
    return n**2 + a * n + b


# print(isPrime(primeFunction(1, 1001, 1)))
# exit()

longestStreak = 0
winningA = 0
winningB = 0
for b in range(1, 1001, 2):
    if isPrime(b):
        for a in range(-1001, 1001, 2):
            i = 0
            while True:
                # print(a, b, i)
                if isPrime(primeFunction(i, a, b)):
                    i += 1
                else:
                    if i > longestStreak:
                        longestStreak = i
                        winningA = a
                        winningB = b
                    break
            # print(a, b, i)

print(winningA, winningB, longestStreak)
print(winningA * winningB)
# print(isPrime(-2))
