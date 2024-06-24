#!/usr/bin/env python3
import csv
from collections import defaultdict

# File path to your CSV file
file_path = 'ipv4.csv'


def find_duplicate_ips(file_path):
    ip_dict = defaultdict(list)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Iterate through each row and store rows by IP with row number
        for row_number, row in enumerate(reader, start=1):
            ip_dict[row['IP']].append((row_number, row))

    # Find and report duplicate IPs
    duplicates = {ip: rows for ip, rows in ip_dict.items() if len(rows) > 1}

    if duplicates:
        print('Duplicate IPs found:')
        for ip, rows in duplicates.items():
            print(f'IP: {ip}')
            for row_number, row in rows:
                print(f'Row {row_number}: {row}')
    else:
        print('No duplicate IPs found.')


if __name__ == '__main__':
    find_duplicate_ips(file_path)
