
#cumulative product


def cumulative_product(numbers):
    result = []
    total = 1
    for number in numbers:
        total *= number
        result.append(total)
    return result

# Example usage
print(cumulative_product([4, 3, 2, 1]))  # Output: [4, 12, 24, 24]