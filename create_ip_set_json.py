#!/usr/bin/env python3
import csv
import json


def create_ip_set_json():
    # Read CSV data from file
    with open('ipset.csv', mode='r') as file:
        reader = csv.DictReader(file)

        # Extract IP addresses
        ip_addresses = [row['IP'] + '/32' for row in reader]

    # Output as JSON array
    print(json.dumps(ip_addresses, indent=4))


if __name__ == '__main__':
    create_ip_set_json()
