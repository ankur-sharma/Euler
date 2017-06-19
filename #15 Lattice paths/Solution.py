#https://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/

# 40! / (20! 20!)

gridSize = 20
dimension = 2

def factorial(number):
    if (number == 1):
        return 1
    return number * factorial(number-1);
    
duplicateDirections = factorial(gridSize)
combinations = factorial(gridSize)

totalMoves = factorial(dimension*gridSize) // (duplicateDirections * combinations)

print(totalMoves)