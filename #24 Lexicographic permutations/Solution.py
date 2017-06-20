
def permute(prefix, suffix):
    global permutationIndex
    global millionthNumber

    if permutationIndex >= million:
        return

    if len(prefix) == 0:
        permutationIndex += 1
        # print(permutationIndex, suffix)
        if permutationIndex == million:
            millionthNumber = suffix[:]
    else:
        for i in range(len(prefix)):
            permute(prefix[0:i] + prefix[i + 1:], suffix + prefix[i:i + 1])


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutationIndex = 0
millionthNumber = []
million = 1000000

permute(digits, [])
print("".join(map(str, millionthNumber)))
