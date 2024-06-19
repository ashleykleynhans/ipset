#!/usr/bin/env python3
import csv
import json

# Read CSV data from file
with open('ipset.csv', mode='r') as file:
    reader = csv.DictReader(file)

    # Extract IP addresses
    ip_addresses = [row['IP'] for row in reader]

# Output as JSON array
print(json.dumps(ip_addresses, indent=4))

