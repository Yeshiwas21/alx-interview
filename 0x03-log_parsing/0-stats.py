#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Regular expression pattern to match the log entry format
LOG_PATTERN = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

def parse_log_line(line):
    """
    Parse a single log line and extract IP address, status code, and file size.
    Return a tuple (ip_address, status_code, file_size).
    """
    match = LOG_PATTERN.match(line)
    if match:
        ip_address, status_code, file_size = match.groups()
        return ip_address, int(status_code), int(file_size)
    else:
        return None

def print_statistics(total_size, status_counts):
    """
    Print statistics including total file size and number of lines by status code.
    """
    print(f'Total file size: {total_size}')
    for status_code in sorted(status_counts.keys()):
        print(f'{status_code}: {status_counts[status_code]}')

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed = parse_log_line(line)
            if parsed:
                _, status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_size, status_counts)
            else:
                continue
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
