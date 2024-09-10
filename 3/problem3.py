import os
import sys
import time

directory = sys.argv[1]

for entry in os.listdir(directory):
    full_path = os.path.join(directory, entry)
    if os.path.isfile(full_path):
        file_stat = os.stat(full_path)
        size = file_stat.st_size
        mod_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_stat.st_mtime))
        print(f"{entry}\t{size}\t{mod_time}")
