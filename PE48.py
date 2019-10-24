# Project Euler: Q48
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
bigNum = 0
for i in range(1001):
    bigNum += i ** i

def individualDigits(num):
    digitsList = []
    while num:
        digitsList.append(num%10)
        num //= 10
    digitsList = digitsList[::-1]
    return digitsList

plentyDigits = individualDigits(bigNum)
plentyDigits = plentyDigits[::-1]
lasTen = []
count  = 0
while count != 10:
    lasTen.append(plentyDigits[count])
    count += 1
print(f"The last ten digits are: {lasTen[::-1]}")
