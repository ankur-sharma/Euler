seqMap = {}

def getCollatzSeqLen(number):
    seqLen = 1
    while number > 1:
        # print(number)
        if number in seqMap:
            return seqLen + seqMap[number]
        
        if number%2==0:
            number//=2
        else:
            number=3*number+1
            
        seqLen+=1
        
    return seqLen;
        
# print(getCollatzSeqLen(1))
for number in range(1, 1000000, 1):
    length = getCollatzSeqLen(number)
    seqMap[number]=length

maxlen = 0    
maxlenNumber = 0
for n in seqMap:
    if seqMap[n] > maxlen:
        maxlenNumber = n
        maxlen = seqMap[n]
        
print(maxlenNumber, maxlen)
