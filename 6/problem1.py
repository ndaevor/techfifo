def product(a, b):
    # Base case: if b is 0, the result is 0
    if b == 0:
        return 0
    # Base case: if b is 1, the result is a
    elif b == 1:
        return a
    # Recursive case: if b is positive
    elif b > 1:
        return a + product(a, b - 1)
    # Handle negative b by converting it to positive
    else:
        return -product(a, -b)

# Example usage:
print(product(3, 4))  # Output: 12
print(product(5, -3)) # Output: -15
print(product(-2, 3)) # Output: -6
print(product(-2, -3))# Output: 6
