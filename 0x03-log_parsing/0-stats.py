#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
from sys import stdin
import re


def print_stats(stats, total_size):
    """prints statistics"""
    print('File size: {}'.format(total_size))
    for record, count in sorted(stats.items()):
        if count:
            print('{}: {}'.format(record, count))


total_size = 0
counter = 0
records = {
    "200": 0, "301": 0,
    "400": 0, "401": 0,
    "403": 0, "404": 0,
    "405": 0, "500": 0
}

p1 = r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
p2 = r'"GET /projects/260 HTTP/1\.1" (200|301|400|401|403|404|405|500) \d+'
pattern = re.compile(p1 + p2)

try:
    for line in stdin:
        processed_line = line.strip()
        if not pattern.fullmatch(processed_line) or len(line.split()) < 4:
            continue
        status_code, file_size = processed_line.split()[-2:]
        counter += 1
        if status_code in records:
            records[status_code] += 1
        total_size += int(file_size)
        if counter == 10:
            counter = 0
            print_stats(records, total_size)
except KeyboardInterrupt:
    pass
finally:
    print_stats(records, total_size)
