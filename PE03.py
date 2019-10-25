# Project Euler: Q3
# Find the largest prime factor of the number 600851475143
primeFactors = []
givenNum = 600851475143
i = 2
while i <= givenNum:
    if(givenNum % i == 0):
        primeFactors.append(i)
        givenNum /= i
    else:
        i += 1
print(f"The largest prime factor for 600851475143 is: {max(primeFactors)}")
