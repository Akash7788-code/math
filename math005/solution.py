import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_multiple(start, end):
    result = 1
    for i in range(start, end + 1):
        result = lcm(result, i)
    return result

start, end = map(int, input("Enter the range of numbers (start,end): ").split(','))
print("Smallest positive number evenly divisible by all numbers from", start, "to", end, "is:", smallest_multiple(start, end))