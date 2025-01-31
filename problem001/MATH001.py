def sum_of_multiples(n, x):
    m = (n - 1) // x  
    return x * m * (m + 1) // 2  

n = 1000
result = sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15) 

print(result)  
