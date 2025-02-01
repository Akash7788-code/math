def sum_even_fibonacci(limit):
    a, b = 2, 8  
    total = 2 

    while b <= limit:
        total += b
        a, b = b, 4 * b + a  

    return total


limit = int(input("Enter the limit: "))
result = sum_even_fibonacci(limit)
print(f"Sum of even Fibonacci numbers below {limit}: {result}")
