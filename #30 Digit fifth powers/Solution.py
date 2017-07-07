fifthPowers = {}
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def compute(digit, index, sumOfDigits, number):
    sumOfDigits += fifthPowers[digit]
    number += digit * 10**index
    return sumOfDigits, number


def undoCompute(digit, index, sumOfDigits, number):
    sumOfDigits -= fifthPowers[digit]
    number -= digit * 10**index
    return sumOfDigits, number


for i in digits:
    fifthPowers[i] = i**5

sumOfDigits = 0
number = 0
sumOfFiftPowerNumbers = 0


for n in range(10, 999999):
    sum = 0
    for i in str(n):
        sum += fifthPowers[int(i)]
    if sum == n:
        sumOfFiftPowerNumbers += n
        print(n)


print("Result = ", sumOfFiftPowerNumbers)
