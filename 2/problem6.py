#reverse

def reverse(lst):
    start, end = 0, len(lst) - 1
    
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst

print(reverse([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]
print(reverse(reverse([1, 2, 3, 4])))  # Output: [1, 2, 3, 4]
