#!/usr/bin/env python3
import argparse
import requests
import json
import pytz
from datetime import datetime
from dotenv import dotenv_values


def get_args():
    parser = argparse.ArgumentParser(
        description='Report a malicious IP to AbuseIPDB',
    )

    parser.add_argument(
        '--ip-address', '-ip-address', '--ip', '-ip', '--i', '-i',
        type=str,
        required=True,
        help='IP Address (eg. 106.75.134.172)'
    )

    parser.add_argument(
        '--categories', '-categories', '--c', '-c',
        type=str,
        required=True,
        help='Categories (eg. 19,21)'
    )

    parser.add_argument(
        '--reason', '-reason', '--r', '-r',
        type=str,
        required=True,
        help='Reason (eg. Malicious Behaviour/Probing for vulnerabilities/Brute force attempts)'
    )

    return parser.parse_args()


def report_to_ipdb():
    env = dotenv_values('.env')
    api_key = env.get('API_KEY', None)
    timezone = env.get('TIMEZONE', None)
    url = 'https://api.abuseipdb.com/api/v2/report'

    now = datetime.now()
    timezone = pytz.timezone(timezone)
    localized_time = timezone.localize(now)
    timestamp = localized_time.strftime('%Y-%m-%dT%H:%M:%S%z')

    params = {
        'ip': ip_address,
        'categories': categories,
        'comment': reason,
        'timestamp': f'{timestamp[:-2]}:{timestamp[-2:]}'
    }

    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }

    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        params=params
    )

    if response.status_code >= 500:
        print(f'Server error: {response.status_code}')
    else:
        decodedResponse = json.loads(response.text)
        print(json.dumps(decodedResponse, sort_keys=True, indent=4))


if __name__ == '__main__':
    args = get_args()
    ip_address = args.ip_address
    categories = args.categories
    reason = args.reason
    report_to_ipdb()
