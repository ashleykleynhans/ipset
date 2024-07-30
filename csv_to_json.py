#!/usr/bin/env python3
import csv
import json


def process_csv_to_json(input_file, output_file):
    # Read the CSV file and filter entries
    filtered_entries = []
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'leakix.org' in row['Hostname']:
                filtered_entries.append({
                    'country': row['Country'],
                    'countryCode': row['Country Code'],
                    'region': row['Region'],
                    'regionName': row['Region Name'],
                    'city': row['City'],
                    'zip': row['ZIP'],
                    'lat': float(row['Latitude']),
                    'lon': float(row['Longitude']),
                    'timezone': row['Timezone'],
                    'isp': row['ISP'],
                    'org': row['Organization'],
                    'as': row['AS'],
                    'ip': row['IP'],
                    'abuse_confidence_score': int(row['Abuse Confidence Score']),
                    'detail': row['Hostname']
                })

    # Write the filtered entries to a JSON file
    with open(output_file, 'w') as jsonfile:
        json.dump(filtered_entries, jsonfile, indent=2)

    return len(filtered_entries)


if __name__ == '__main__':
    input_file = 'ipv4.csv'
    output_file = 'leakix.json'
    entries_processed = process_csv_to_json(input_file, output_file)
    print(f'Processed {entries_processed} entries. Results saved to {output_file}')
