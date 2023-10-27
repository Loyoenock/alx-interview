#!/usr/bin/python3
import sys


def print_message(status_codes, total_file_size):
    """

    Print the file size and counts of status codes.
        Args:
        status_codes (dictionery)
        total_file_size (int): The total file size.
    Returns:
        None
    """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print(f"{code}: {count}")

total_file_size = 0
code = 0
counter = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]  # Reverse the parsed line

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # Get file size
                code = parsed_line[1]  # Get status code

                if code in status_codes:
                    status_codes[code] += 1

            if counter == 10:
                print_message(status_codes, total_file_size)
                counter = 0

finally:
    print_message(status_codes, total_file_size)
