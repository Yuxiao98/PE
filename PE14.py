# Project Euler: Q14
# Find the starting number, under one million, produces the longest chain
def eachChainLen(n):
    chainLen = 0
    while n!= 1:
        if(n % 2 == 0):
            n = n/2
        else:
            n = 3*n + 1
        chainLen += 1

    if n == 1:
        return chainLen+1
    
currLen = 0
maxLen = 10
theNumberWeNeed = 13
for i in range(1000000, 13, -1):
    currLen = eachChainLen(i)
    if currLen > maxLen:
        maxLen = currLen
        theNumberWeNeed = i
print(maxLen)
print(theNumberWeNeed)
