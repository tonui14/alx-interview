#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    """Print the accumulated metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption."""
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
for line in sys.stdin:
    line_count += 1
    parts = line.split()

    # Check if line format is valid
    if len(parts) < 7:
        continue  # Skip invalid lines

    # Extract the file size and status code
    try:
        status_code = int(parts[5])
        file_size = int(parts[6])
    except (ValueError, IndexError):
        continue  # Skip if not convertible to int

    # Update metrics
    total_file_size += file_size
    if status_code in status_codes_count:
        status_codes_count[status_code] += 1

    # Print metrics every 10 lines
    if line_count % 10 == 0:
        print_metrics()

# Final output if the script finishes without interruption
print_metrics()
