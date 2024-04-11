#!/usr/bin/python3
import sys
import re

def compute_stats(lines):
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for line in lines:
        match = re.match(r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)
        if match:
            _, _, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        else:
            print(f"Skipping line: {line.strip()}")

    return total_size, status_counts

def main():
    lines = []
    try:
        for i, line in enumerate(sys.stdin):
            lines.append(line.strip())
            if (i + 1) % 10 == 0:
                total_size, status_counts = compute_stats(lines)
                print(f"File size: {total_size}")
                for status, count in sorted(status_counts.items()):
                    if count > 0:
                        print(f"{status}: {count}")
                print()
                lines = []
    except KeyboardInterrupt:
        total_size, status_counts = compute_stats(lines)
        print(f"File size: {total_size}")
        for status, count in sorted(status_counts.items()):
            if count > 0:
                print(f"{status}: {count}")

if __name__ == "__main__":
    main()
