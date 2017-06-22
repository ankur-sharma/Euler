firstFibonacci = 1
secondFibonacci = 1

index = 2
while True:
    nextFibonacci = firstFibonacci + secondFibonacci
    index += 1
    if len(str(nextFibonacci)) == 1000:
        print(nextFibonacci)
        break
    firstFibonacci = secondFibonacci
    secondFibonacci = nextFibonacci

print(index)
