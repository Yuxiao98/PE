# Project Euler: Q4
# Find the largest palindrome made from the product of two 3-digit numbers.
def individualDigits(num):
    digitsList = []
    while num:
        digitsList.append(num%10)
        num //= 10
    digitsList = digitsList[::-1]
    return digitsList
palindromeNums = []
for i in range(10000, 1000000):
    firstHalf = individualDigits(i)[:len(individualDigits(i))//2]
    lastHalf = individualDigits(i)[len(individualDigits(i))//2:]
    re_lastHalf = lastHalf[::-1]
    if firstHalf == re_lastHalf:
        palindromeNums.append(i)
maxPali = 100001
maxFactors = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if i*j in palindromeNums:
            if i*j > maxPali:
                maxPali = i*j
                maxFactors = [i, j]
print(f"The max palindrome number is: {maxPali}, which has factors: {maxFactors}")
