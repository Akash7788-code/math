def sum_square_difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares

n = int(input("Enter a number for sum square difference: "))
print("Difference between sum of squares and square of sum for first", n, "natural numbers is:", sum_square_difference(n))
