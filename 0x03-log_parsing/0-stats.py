#!/usr/bin/python3
""" Log parsing script """
import sys


status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0
                }

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_split = line.split()
        if len(line_split) > 4:
            code = line_split[-2]
            file_size = int(line_split[-1])
            if code in status_codes.keys():
                status_codes[code] += 1
            total_size += file_size
            line_count += 1
            if line_count == 10:
                line_count = 0
                print('File size: {}'.format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
