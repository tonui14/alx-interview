#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""
import sys

def print_stats(total_size, status_counts):
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    """Main function to process the log lines."""
    total_size = 0
    status_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            line_count += 1

            try:
                parts = line.split()
                if len(parts) < 7:
                    continue

                file_size = int(parts[-1])
                status_code = parts[-2]

                total_size += file_size

                if status_code.isdigit():
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1
            except (ValueError, IndexError):
                continue

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
