import os
import sys

directory = sys.argv[1]

for entry in os.listdir(directory):
    print(entry)
