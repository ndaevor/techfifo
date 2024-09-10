#duplicates

def dups(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# Example usage
print(dups([1, 2, 2, 3, 4, 4, 5]))  # Output: [2, 4]
print(dups(['apple', 'banana', 'apple', 'cherry', 'banana']))  # Output: ['apple', 'banana']
