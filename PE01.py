# Projec Euler: Q01
# Find the sum of all the multiples of 3 or 5 below 1000
theFinalSumIAmExpectingTo = 0
for i in range(1000):
    if(i % 3 == 0 or i % 5 == 0):
        theFinalSumIAmExpectingTo += i
print(theFinalSumIAmExpectingTo)
