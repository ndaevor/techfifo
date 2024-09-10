#product function to find product of elements in a list

def product(numbers):
    result = 1
    for number in numbers:
        result *= number  
    return result 


print(product([1, 2, 3]))  # Output: 6
print(product([4, 5, 6]))  # Output: 120
print(product([7]))        # Output: 7
print(product([]))         # Output: 1 (product of an empty list is conventionally 1)
