# Project Euler: Q34
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
import math
def individualDigits(num):
    digitsList = []
    while num:
        digitsList.append(num%10)
        num //= 10
    digitsList = digitsList[::-1]
    return digitsList

magicSet = set()
for i in range(math.factorial(9)):
    digitsSum = 0
    digits = individualDigits(i)
    for digit in digits:
        digitsSum += math.factorial(digit)
    if digitsSum == i:
        magicSet.add(i)
print(f"The sum of curious numbers is: {sum(magicSet) - 3}")
