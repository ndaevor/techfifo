#output of the following program

x = [0, 1, [2]]
x[2][0] = 3
print(x)
x[2].append(4)
print(x)
x[2] = 2
print(x)

"""
output
[0, 1, [3]]
[0, 1, [3, 4]]
[0, 1, 2]


x = [0, 1, [2]]  # Initialize a list with elements 0, 1, and a nested list [2]
x[2][0] = 3     # Modify the first element of the nested list [2] to 3
print(x)        # [0, 1, [3]]
x[2].append(4)  # Append the value 4 to the nested list [3]
print(x)        # [0, 1, [3, 4]]
x[2] = 2        # Replace the nested list [3, 4] with the integer 2
print(x)        # [0, 1, 2]



"""