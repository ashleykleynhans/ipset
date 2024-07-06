#!/usr/bin/env python3
import csv

input_file = 'ipv4.csv'
output_file = 'filtered_ipv4.csv'

with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    header = next(reader)  # Read the header row

    # Find the index of the 'Abuse Confidence Score' column
    try:
        abuse_score_index = header.index('Abuse Confidence Score')
    except ValueError:
        print("Error: 'Abuse Confidence Score' column not found in the CSV file.")
        exit(1)

    writer = csv.writer(outfile)
    writer.writerow(header)  # Write the header to the output file

    for row in reader:
        try:
            abuse_score = float(row[abuse_score_index])
            if abuse_score >= 2:
                writer.writerow(row)
        except (IndexError, ValueError):
            print(f"Warning: Skipping row due to invalid data: {row}")

print(f"Filtered data has been written to {output_file}")
