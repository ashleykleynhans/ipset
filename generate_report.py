#!/usr/bin/env python3
import csv
from collections import defaultdict
import ipaddress


def ip_to_int(ip):
    return int(ipaddress.ip_address(ip))


def int_to_ip(int_ip):
    return str(ipaddress.ip_address(int_ip))


def find_ip_ranges(ips):
    ips = sorted(set(ips), key=ip_to_int)
    ranges = []
    start = end = ip_to_int(ips[0])

    for ip in ips[1:]:
        current = ip_to_int(ip)
        if current == end + 1:
            end = current
        else:
            ranges.append((int_to_ip(start), int_to_ip(end)))
            start = end = current

    ranges.append((int_to_ip(start), int_to_ip(end)))
    return ranges


def format_range(start, end):
    if start == end:
        return start
    return f"{start}-{end}"


def main():
    # Read CSV and group by ASN
    asn_groups = defaultdict(list)
    with open('ipv4.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ip = row['IP']
            asn = row['AS']
            asn_groups[asn].append(ip)

    # Find common IP ranges for each ASN with at least 10 IPs
    asn_ranges = {}
    for asn, ips in asn_groups.items():
        if len(ips) >= 10:
            ranges = find_ip_ranges(ips)
            asn_ranges[asn] = ranges

    # Sort ASNs by frequency (number of IPs)
    sorted_asns = sorted(
        asn_ranges.items(),
        key=lambda x: len(asn_groups[x[0]]),
        reverse=True
    )

    # Print results in markdown format
    print("# IP Ranges Grouped by ASN (10+ IPs)")
    print()

    for asn, ranges in sorted_asns:
        print(f"## {asn}")
        print(f"**Total IPs:** {len(asn_groups[asn])}")
        print()
        print("### IP Ranges:")
        for start, end in ranges:
            print(f"- `{format_range(start, end)}`")
        print()


if __name__ == "__main__":
    main()
