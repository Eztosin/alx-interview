#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys

total_size = 0
count_status_code = {}

for line in sys.stdin:
    try:
        _, _, _, _, _,status_code, file_size = line.strip().split()

        # Converting file size to an int
        file_size = int(file_size)

        # Updating total file size
        total_size += file_size

        # Update status code counts
        if status_code.isdigit():
            status_code = int(status_code)
            count_status_code[status_code] = count_status_code.get(status_code, 0) + 1

        if len(count_status_code) % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(count_status_code.keys()):
                print("code: {}".format(count_status_code[code]))

    except ValueError:
        pass

print("File size: {}".format(total_size))
for code in sorted(count_status_code.keys()):
    print("code: {}".format(count_status_code[code]))
