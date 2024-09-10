#factorial

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(4))  # Output: 24
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
