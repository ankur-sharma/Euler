# not the best written code but that's what you get at 2AM
from decimal import *


def getRecurringCycle(number):
    if "." not in number:
        return 0, ""

    dot = number.index(".")
    number = number[dot + 1:]
    n = len(number)
    length = n
    recur = ""
    for i in range(n + 1):
        for j in range(i + 1, n - i):
            p = number[i:j]
            temp = (number[0:i] + p * (1 + n // (j - i)))[0:n]
            if number == temp and j - i < n and j - i < length:
                length = j - i
                recur = p
                return length, p

    return length, recur


maxD = 1
maxLength = 0
maxRecur = ""
getcontext().prec = 1000
getcontext().rounding = ROUND_FLOOR
for d in range(1, 1000):
    if d % 2 == 0 or d % 3 == 0 or d % 5 == 0:  # ideally run checks for only prime numbers
        continue

    factor = Decimal(1) / Decimal(d)
    recurringCycleLength, recur = getRecurringCycle(str(factor))
    if recurringCycleLength > maxLength:
        maxLength = recurringCycleLength
        maxD = d
        maxRecur = recur

print()
print(maxD, maxLength, Decimal(1) / Decimal(maxD), maxRecur)
