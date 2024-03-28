#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys

# Store the count of all status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # Keep count of the number of lines counted

try:
    for line in sys.stdin:
        line_list = line.split()

        if len(line_list) > 7 and line_list[5] == '"GET' and line_list[6] == '/projects/260' and line_list[7].startswith('HTTP/'):
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Check if the status code received exists in the dictionary and increment its count
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

            # Update total size
            total_size += file_size

            # Update count of lines
            count += 1

        if count == 10:
            count = 0  # Reset count
            print('File size:', total_size)

            # Print out status code counts
            for key in sorted(status_codes_dict.keys(), key=lambda x: int(x)):
                if status_codes_dict[key] != 0:
                    print('{}: {}'.format(key, status_codes_dict[key]))

except KeyboardInterrupt:
    pass

finally:
    # Print final statistics
    print('File size:', total_size)
    for key in sorted(status_codes_dict.keys(), key=lambda x: int(x)):
        if status_codes_dict[key] != 0:
            print('{}: {}'.format(key, status_codes_dict[key]))
