def factorial(number):
    if number == 1:
        return 1
    return number*factorial(number-1)
    
factorialHundred = factorial(100)

sumOfDigits = 0
for i in str(factorialHundred):
    sumOfDigits+=int(i)
    
print(sumOfDigits)