#!/usr/bin/python3
import sys

def main():
    status_counts = {}
    total_file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split()

            if len(parts) >= 7:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update total file size
                total_file_size += file_size

                # Update status code counts
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(total_file_size, status_counts)

def print_statistics(total_file_size, status_counts):
    print(f"Total file size: {total_file_size} bytes")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

if __name__ == "__main__":
    main()
