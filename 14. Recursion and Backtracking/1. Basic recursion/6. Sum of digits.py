def sum_of_digits(n):
    # Base case: if the number becomes 0, stop the recursion
    if n == 0:
        return 0
    
    # Recursive case: last digit + sum of the remaining digits
    return (n % 10) + sum_of_digits(n // 10)

# Example usage
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")
