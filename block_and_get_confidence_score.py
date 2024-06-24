#!/usr/bin/env python3
import csv
import json
import requests
import time
import pytz
from datetime import datetime
from dotenv import dotenv_values

ABUSE_IPDB_REASON = 'Malicious Behaviour/Probing for vulnerabilities/Brute force attempts'
ABUSE_IPDB_CATEGORIES = [
    '19',
    '21'
]


def report_to_abuse_ipdb(ip_address):
    env = dotenv_values('.env')
    api_key = env.get('API_KEY', None)
    timezone = env.get('TIMEZONE', None)
    abuse_confidence_score = None

    now = datetime.now()
    timezone = pytz.timezone(timezone)
    localized_time = timezone.localize(now)
    timestamp = localized_time.strftime('%Y-%m-%dT%H:%M:%S%z')

    params = {
        'ip': ip_address,
        'categories': ','.join(ABUSE_IPDB_CATEGORIES),
        'comment': ABUSE_IPDB_REASON,
        'timestamp': f'{timestamp[:-2]}:{timestamp[-2:]}'
    }

    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }

    response = requests.request(
        method='POST',
        url='https://api.abuseipdb.com/api/v2/report',
        headers=headers,
        params=params
    )

    if response.status_code >= 500:
        print(f'Server error: {response.status_code}')
    else:
        decodedResponse = json.loads(response.text)
        abuse_confidence_score = decodedResponse['data']['abuseConfidenceScore']

    return abuse_confidence_score


if __name__ == '__main__':
    # Read CSV data from file
    with open('reputation_lookup.csv', mode='r') as csv_input_file:
        reader = csv.DictReader(csv_input_file)
        i = 0

        with open('ipv4.csv', 'a') as csv_output_file:
            writer = csv.writer(csv_output_file)

            # Write header row if the output file is empty
            if csv_output_file.tell() == 0:
                writer.writerow([
                    'Date Added',
                    'IP',
                    'Abuse Confidence Score',
                    'Country',
                    'Country Code',
                    'Region',
                    'Region Name',
                    'City',
                    'ZIP',
                    'Latitude',
                    'Longitude',
                    'Timezone',
                    'ISP',
                    'Organization',
                    'AS'
                ])

            for row in reader:
                ip_address = row['IP']
                print(f'Reporting IP address {ip_address} to AbuseIPDB')
                abuse_confidence_score = report_to_abuse_ipdb(ip_address)

                writer.writerow([
                    row['Date Added'],
                    ip_address,
                    abuse_confidence_score,
                    row['Country'],
                    row['Country Code'],
                    row['Region'],
                    row['Region Name'],
                    row['City'],
                    row['ZIP'],
                    row['Latitude'],
                    row['Longitude'],
                    row['Timezone'],
                    row['ISP'],
                    row['Organization'],
                    row['AS']
                ])

                i += 1
                if i % 45 == 0:  # Respect the 45 requests per minute limit
                    print('Sleeping for 60 seconds...')
                    time.sleep(60)  # Wait for 60 seconds
