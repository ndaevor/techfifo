def cumulative_sum(numbers):
    result = []
    total = 0
    for number in numbers:
        total += number
        result.append(total)
    return result

# Example usage
print(cumulative_sum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]


def cumulative_concatenate(strings):
    result = []
    cumulative = ""
    for string in strings:
        cumulative += string
        result.append(cumulative)
    return result

# Example usage
print(cumulative_concatenate(["a", "b", "c", "d"]))  # Output: ['a', 'ab', 'abc', 'abcd']
