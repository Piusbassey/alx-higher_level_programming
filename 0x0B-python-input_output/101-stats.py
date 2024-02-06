#!/usr/bin/python3
import sys

def compute_metrics():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        lines_processed = 0
        for line in sys.stdin:
            lines_processed += 1
            parts = line.split()
            if len(parts) >= 9:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if lines_processed % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

def print_stats(total_size, status_counts):
    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

if __name__ == "__main__":
    compute_metrics()
