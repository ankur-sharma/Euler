# n.!n < !(n+1) 
# it can not be more than a 7 digit number as 8*!9 is a 7 digit number
# sum(!n) < !(n+1)

import time

def permute(prefix, suffix, r):
    if len(suffix) == r:
        yield suffix
        return
    for i in range(len(prefix)):
        yield from permute(prefix, suffix + prefix[i:i+1], r)
        

def main():
    digits = [0,1,2,3,4,5,6,7,8,9]
    factorials = {0:1}
    factorialDigitLen = {i:9 for i in digits}
    n = 1
    for i in digits[1:]:
        n *= i
        factorials[i] = n
        factorialDigitLen[len(str(n))]=i
        
    
    sumOfDigitFactorialNumbers = 0
    for numberOfDigits in range(2,7):
        useDigits = factorialDigitLen[numberOfDigits]+1
        generator = permute(digits[:useDigits], [], numberOfDigits)
        for n in generator:
            if n[0] == 0:
                continue
            sumOfDigitFactorials = 0
            number = int("".join(map(str, n)))
            for x in n:
                sumOfDigitFactorials += factorials[x]
                if sumOfDigitFactorials == number:
                    print("Digit Factorial Number", number)
                    sumOfDigitFactorialNumbers += number

    print("Sum of Digit Factorials", sumOfDigitFactorials)

#main2 is still faster than main
#optimizations were useless
def main2():
    digits = [0,1,2,3,4,5,6,7,8,9]
    factorials = {0:1}
    factorialDigitLen = {i:9 for i in digits}
    n = 1
    for i in digits[1:]:
        n *= i
        factorials[i] = n
        factorialDigitLen[len(str(n))]=i    

    sumOfDigitFactorialNumbers = 0
    for n in range(10, 999999):
        sumOfDigitFactorials = 0
        for x in str(n):
            sumOfDigitFactorials += factorials[int(x)]
            if sumOfDigitFactorials == n:
                print("Digit Factorial Number", n)
                sumOfDigitFactorialNumbers += n
                
    print("Sum of Digit Factorials", sumOfDigitFactorialNumbers)
                
start_time = time.time()
main2()
print("--- %s seconds ---" % (time.time() - start_time))