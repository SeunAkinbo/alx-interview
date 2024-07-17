#!/usr/bin/env python3
"""Module - 0-stats.py"""
import sys
import signal

total_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

def print_statistics():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 10:
            continue
        
        ip, dash, date, method, path, protocol, status, size = parts[0], parts[1], parts[3], parts[4], parts[5], parts[6], parts[8], parts[9]
        
        if method != '"GET' or protocol != 'HTTP/1.1"' or path != '/projects/260':
            continue
        
        try:
            total_size += int(size)
        except ValueError:
            continue
        
        if status in status_codes_count:
            status_codes_count[status] += 1
        
        line_count += 1
        
        if line_count % 10 == 0:
            print_statistics()
except Exception as e:
    pass
finally:
    print_statistics()
