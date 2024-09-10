#compare 2 strings ignoring case

def istrcmp(str1, str2):
    return str1.lower() == str2.lower()
print(istrcmp('python', 'Python'))  # True
print(istrcmp('LaTeX', 'Latex'))   # True
print(istrcmp('a', 'b'))           # False


"""
output
true 
true
false
"""