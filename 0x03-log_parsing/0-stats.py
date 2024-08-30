#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
from sys import stdin
import re


def print_stats(stats):
    """prints statistics"""
    print('File size:', total_size)
    for record, count in stats.items():
        if count:
            print(f'{record}: {count}')


total_size = 0
counter = 0
records = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

p1 = r'(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
p2 = r'"GET /projects/260 HTTP/1.1" (200|301|400|401|403|404|405|500) \d+'
pattern = re.compile(p1 + p2)

try:
    for line in stdin:
        line = line.strip()
        if not pattern.fullmatch(line):
            continue
        status_code, file_size = line.split()[-2:]
        if counter == 10:
            counter = 0
            print_stats(records)
        else:
            count = records.get(status_code)
            if count is not None:
                records[status_code] = count + 1
            total_size += int(file_size)
        counter += 1
except KeyboardInterrupt:
    print_stats(records)
    raise
