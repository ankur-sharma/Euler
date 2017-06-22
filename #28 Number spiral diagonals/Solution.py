# for spiral dimension d
# Left up diagonal = 1, 9, 25, 49, ... = 1^2, 3^2, 5^2, 7^2...(2n+1)^2
# Right up diagonal = 1, 7, 21, 43, 73... = 1^2-(1.1-1), 3^2-(1.3-1), 5^2-(1.5-1), 7^2-(1.7-1)....(2n+1)^2-2n
# Rigth down diagonal = 1, 5, 17, 37, 65,... = 1^2-(2.1-2), 3^2-(2.3-2), 5^2-(2.5-2), 7^2-(2.7-2).....(2n+1)^2-4n
# Left down diagonal = 1, 3, 13, 31, 57, ... = 1^2-0, 3^2-(3.3-3), 5^2-(3.5-3)

# sum = 4((2n+1)^2 - 12n


def diagonalSum(n):

    print(n)
    dSum = 0
    for i in range(0, n + 1, 1):
        s = 4 * (2 * i + 1)**2 - 12 * i
        dSum += s
    return dSum


dimension = 1001
n = dimension // 2
print(diagonalSum(n) - 3)
