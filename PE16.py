# Project Euler: Q16
# Find the sum of digits of number 2^1000
r = 0
n = 2**1000
while n:
    r += n % 10
    n //= 10
print(r)
