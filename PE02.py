# Project Euler: Q2
# Find the sum of the even-valued terms(do not exceed four million)
fibonacci_numbers = [0,1]
finalNum = 0
i = 2
while True:
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    i += 1
    if(fibonacci_numbers[i- 1] > 4000000):
        break
    elif(fibonacci_numbers[i-1] % 2 == 0):
        finalNum += fibonacci_numbers[i - 1]
print(f"The sum of even-valued terms is: {finalNum}")
