# Project Euler: Q07
# Find the 10001st prime number.
import math
primeList = []
for num in range(2,2000000):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       primeList.append(num)
print(primeList[10001])
