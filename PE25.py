# Project Euler: Q25
# Find the index of the first term in the Fibonacci sequence to contain 1000 digits
def countDigits(num):
    c = 0
    while num:
        num //= 10
        c += 1
    return c

fibonacci_numbers = [0, 1]
i = 2
while True:
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    i += 1
    if(countDigits(fibonacci_numbers[len(fibonacci_numbers)-1]) == 1000):
        break
print(f"The index of the first number containing 1000 digits is: {i-1}")
