

def lensort(strings):
    # Sort the list of strings based on the length of each string
    return sorted(strings, key=len)

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
# Output: ['c', 'perl', 'java', 'ruby', 'python', 'haskell']
