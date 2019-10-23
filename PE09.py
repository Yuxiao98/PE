# Project of Euler: Q9
# There exits exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
for a in range(500):
    for b in range(a+1, 500):
        for c in range(b+1, 500):
            if (a*a + b*b == c*c)&(a+b+c==1000):
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                break
