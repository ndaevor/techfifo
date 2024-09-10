#unique in a list

def unique(lst):
    return list(set(lst))

print(unique([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(unique(['apple', 'banana', 'apple', 'cherry']))  # Output: ['apple', 'banana', 'cherry']
