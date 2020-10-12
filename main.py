# Find the greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b

    return a
    # pass


print(gcd(20, 8))
print(gcd(60, 96))

# Next