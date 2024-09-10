def extsort(files):
    # Sort files based on their extensions using a lambda function
    return sorted(files, key=lambda filename: filename.split('.')[-1])

print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
# Output: ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
