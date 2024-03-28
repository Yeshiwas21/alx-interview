#!/usr/bin/python3
"""
Read stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>, skip line if not this format
After every 10 minutes or keyboard interrupt (CTRL + C)
print these from beginning: number of lines by status code
possible status codes: 200, 301, 400, 401, 404, 405, and 500
if status code isn't an integer, do not print it
format: <status code>: <number>
Status code must be printed in ascending order
"""
import sys
import time

def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items(), key=lambda x: int(x[0])):
        if val != 0:
            print("{}: {}".format(key, val))

file_size = 0
count_lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

start_time = time.time()

try:
    for line in sys.stdin:
        parsed_line = line.split()

        if len(parsed_line) == 7:  # Checking if the line has all required components
            count_lines += 1
            file_size += int(parsed_line[-1])  # Last element is file size
            code = parsed_line[-2]  # Second last element is status code

            if code in codes:
                codes[code] += 1

            if time.time() - start_time >= 600:  # Check if 10 minutes have passed
                print_msg(codes, file_size)
                start_time = time.time()
                count_lines = 0
                file_size = 0
                codes = {key: 0 for key in codes}

except KeyboardInterrupt:
    pass  # Do nothing if interrupted

finally:
    print_msg(codes, file_size)  # Print final statistics
