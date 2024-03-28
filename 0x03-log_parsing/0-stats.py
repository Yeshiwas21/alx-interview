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

def print_statistics(status_counts, total_file_size):
    print("File size:", total_file_size)
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_file_size = 0
start_time = time.time()
lines_processed = 0

try:
    for line in sys.stdin:
        # Parse the line
        parts = line.strip().split()
        if len(parts) != 7:
            continue

        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update metrics
        if status_code.isdigit() and status_code in status_counts:
            status_counts[status_code] += 1
            total_file_size += file_size
            lines_processed += 1

        # Check if 10 minutes have elapsed
        if time.time() - start_time >= 600:
            print_statistics(status_counts, total_file_size)
            start_time = time.time()
            lines_processed = 0
            total_file_size = 0
            status_counts = {
                "200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "404": 0,
                "405": 0,
                "500": 0
            }

        # Check if 10 lines have been processed
        if lines_processed == 10:
            print_statistics(status_counts, total_file_size)
            lines_processed = 0
            total_file_size = 0
            status_counts = {
                "200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "404": 0,
                "405": 0,
                "500": 0
            }

except KeyboardInterrupt:
    # Print final statistics if interrupted
    print_statistics(status_counts, total_file_size)
