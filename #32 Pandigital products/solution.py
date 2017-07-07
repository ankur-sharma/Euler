# Heuristics
# Product can not be 5 digit or more because it would leave too few digits for multiplicand and multiplier
# Product can not be 3 digit for less as that would have too many digits left to get a 3 digit number
# Product has to be 4 digit number
# multiplicand and multiplier can either be 1 digit and 4 digit or 2 digit and 3 digit
# when multiplicand is 1 digit then the number can not be 1 or 9
# multiplicand or multiplier can not end of 1

def isPanDigital(n):
    s = str(n)
    if len(s) != 9 or s.find("0") > 0:
        return False
    for i in range(len(s)):
        if s[i] in s[:i] + s[i+1:]:
            return False
    return True
    
        
def permute(prefix, suffix, r):
    if len(suffix) == r:
        yield suffix
    
    for i in range(len(prefix)):
        yield from permute(prefix[:i] + prefix[i+1:], suffix + prefix[i:i+1], r)    
    
    
digits = [1,2,3,4,5,6,7,8,9]
products = []


for l in range(1, 3):
    generator = permute(digits,[], l)
    for m in generator:
        if m[-1] == 1:
            continue
        multiplicand = digits[:]
        for i in m:
            multiplicand.remove(i)
        generator2 = permute(multiplicand,[], 5-l)
        multiplier = int("".join([str(i) for i in m]))
        for n in generator2:
            if n[-1] == 1:
                continue
            number = int("".join([str(i) for i in n]))
            product = multiplier * number
            if product > 9999:
                break
            if isPanDigital(str(multiplier) + str(number) + str(product)):
                print(multiplier, "*", number, "=", product)
                if product not in products:
                    products.append(product)

print("Sum of unique products = ", sum(products))




# def perm(n, i):
#     if i == len(n) - 1: 
#         print("p=", n)
#     else:
#         for j in range(i, len(n)):
#             n[i], n[j] = n[j], n[i]
#             perm(n, i + 1)
#             n[i], n[j] = n[j], n[i] # swap back, for the next loop


# def permute(prefix, suffix):
#     if len(prefix) == 0:
#         print(suffix)
    
#     for i in range(len(prefix)):
#         permute(prefix[:i] + prefix[i+1:], suffix + prefix[i:i+1])