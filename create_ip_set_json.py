#!/usr/bin/env python3
import csv
import ipaddress


def create_ip_set_json():
    # Read CSV data from file
    with open('ipv4.csv', mode='r') as file:
        reader = csv.DictReader(file)

        # Extract IP addresses
        ip_list = [row['IP'] + '/32' for row in reader]

    # Convert to a list of IP networks and sort
    sorted_ip_list = sorted(ip_list, key=lambda ip: ipaddress.ip_network(ip, strict=False))

    # Output the sorted list in list format with each IP on a new line
    output_list = "[\n" + ",\n".join(f'    "{ip}"' for ip in sorted_ip_list) + "\n]"
    print(output_list)


if __name__ == '__main__':
    create_ip_set_json()
