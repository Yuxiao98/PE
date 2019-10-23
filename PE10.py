import math
# Project Euler: Q10
# Find the sum of all the primes below two million.
primeList = []
for num in range(2,2000000):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       primeList.append(num)
print(sum(primeList))
