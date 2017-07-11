#Even number can not be Base 2 palindrome

def isBase10Palindrome(n):
    number = str(n)
    return number == number[::-1]

def isBase2Palindrome(n):
    number = str(bin(n))[2:]
    return number == number[::-1]

sumOfPalindromes = 0    
for n in range(1,1000000,2):
    if isBase10Palindrome(n) and isBase2Palindrome(n):
        sumOfPalindromes += n
        
print(sumOfPalindromes)