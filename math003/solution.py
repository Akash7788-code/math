def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(n):
    max_num = 10**n - 1
    min_num = 10**(n-1)
    largest_palindrome = 0
    
    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):  # Avoid redundant calculations
            product = i * j
            if product <= largest_palindrome:
                break  # No need to check smaller products
            if is_palindrome(product):
                largest_palindrome = product
    
    return largest_palindrome

n = int(input("Enter the number of digits: "))
print("Largest palindrome product:", largest_palindrome_product(n))