import sys
import re


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    line_count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            match = re.match(r'\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)', line)
            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        print("Program interrupted by user.")


if __name__ == "__main__":
    main()
