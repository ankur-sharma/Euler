file = open("p022_names.txt","r")
data = file.readline()
n = len(data)

nameList = []
for name in data.split(","):
    nameList.append(name)

nameList.sort()
index = 0
sumOfNameScores = 0
for name in nameList:
    nameScore = 0
    index += 1
    for c in name:
        if c != "\"":
            nameScore += ord(c) - 64

    
    sumOfNameScores += nameScore * index
        
file.close()

print(sumOfNameScores)
