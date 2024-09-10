#output of the problem

print(2 < 3 and 3 > 1)
# Both conditions are True
# 2 < 3 evaluates to True
# 3 > 1 evaluates to True
# True and True results in True

print(2 < 3 or 3 > 1)
# At least one condition is True
# 2 < 3 evaluates to True
# 3 > 1 evaluates to True
# True or True results in True


print(2 < 3 or not 3 > 1)
# At least one condition is True
# 2 < 3 evaluates to True
# 3 > 1 evaluates to True, so not 3 > 1 evaluates to False
# True or False results in True

print(2 < 3 and not 3 > 1)
# Both conditions need to be True
# 2 < 3 evaluates to True
# 3 > 1 evaluates to True, so not 3 > 1 evaluates to False
# True and False results in False

"""
output
True
True
True
False
"""