import math

def primeDivisors(number):
    n = number
    primeDivisors=[]
        
    end = int(math.pow(n, 0.5))+1
    for i in range(1, end, 1):
        if (n%i==0):
            primeDivisors.append(i)
            primeDivisors.append(number//i)
            
    
    primeDivisors.append(number)
    return len(primeDivisors)
    
def getnerateTriangular(limit):
    found = False
    index = 3
    while(primeDivisors((index*(index+1))//2) < limit):
        index+=1
        
    print(index, (index*(index+1))//2, primeDivisors((index*(index+1))//2))

    
    
getnerateTriangular(500)
