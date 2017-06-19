import math

twoPowerThousand = 2 << 999

print("Two raised to 1000 is ", twoPowerThousand)

sumOfDigits = 0
for i in str(twoPowerThousand):
    sumOfDigits+=int(i)
    
print("Sum of digits is ", sumOfDigits)
    