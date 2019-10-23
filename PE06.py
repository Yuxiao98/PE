# Project of Euler: Q6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum4sqr = 0
sqrSum = 0
for i in range(100):
    sum4sqr += i
    sqrSum += i * i

sum4sqr *= sum4sqr
print(sqrSum)
print(sum4sqr)
print(sum4sqr - sqrSum)
