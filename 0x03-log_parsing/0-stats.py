#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 9:
            continue

        # Extracting file size
        try:
            file_size = int(parts[-1])
            total_size += file_size
        except ValueError:
            continue

        # Extracting status code
        try:
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            continue

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    # Handle Ctrl + C interruption and print accumulated stats
    print_stats(total_size, status_codes)
    raise

# Print final stats when the program ends
print_stats(total_size, status_codes)

