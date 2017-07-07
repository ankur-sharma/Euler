import math
# Equatione One = (10a+b)/(10b+c) = a/c
# 9ac + bc - 10ab = 0
def getEquationOne(a,b,c):
    if 9*a*c + b*c - 10*a*b == 0 and a/c < 1:
        return 10*a+b, 10*b+c
    return 0,0
    
    
# Equatione Two = (10a+b)/(10c+a) = b/c
# 9bc + ab - 10ac = 0
def getEquationTwo(a,b,c):
    if 9*b*c + a*b - 10*a*c == 0 and b/c < 1:
        return 10*a+b, 10*c+a
    return 0,0

def getReducedDenominator(x,y):
    if y % x == 0:
        return y // x
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            if y % i == 0:
                return getReducedDenominator(x//i, y//i)
            elif y % (x//i) == 0:
                return getReducedDenominator(x//(x//i), y//(x//i))
    return y
    
digits = [1,2,3,4,5,6,7,8,9]
numeratorProduct = 1
denominatorProduct = 1

for a in digits:
    for b in digits:
        if a == b:
            continue
        for c in digits:
            if a == c or b == c:
                continue
            x,y = getEquationOne(a,b,c)
            if x == 0:
                x,y = getEquationTwo(a,b,c)
            if x != 0:
                print(x,y)
                numeratorProduct *= x
                denominatorProduct *= y


print(getReducedDenominator(numeratorProduct,denominatorProduct))
