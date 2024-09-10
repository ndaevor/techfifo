#reverse lines in a file
import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end='',)
    print('\n')
