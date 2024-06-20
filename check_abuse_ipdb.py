#!/usr/bin/env python3
import argparse
import requests
import json
from dotenv import dotenv_values


def get_args():
    parser = argparse.ArgumentParser(
        description='Check whether an IP has been reported to AbuseIPDB',
    )

    parser.add_argument(
        '--ip-address', '-ip-address', '--ip', '-ip', '--i', '-i',
        type=str,
        required=True,
        help='IP Address (eg. 106.75.134.172)'
    )

    parser.add_argument(
        '--verbose', '-verbose', '--v', '-v',
        type=bool,
        required=False,
        default=False,
        help='Verbose Output'
    )

    return parser.parse_args()


def check_abuse_ipdb():
    env = dotenv_values('.env')
    api_key = env.get('API_KEY', None)
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }

    if verbose:
        querystring['verbose'] = ''

    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }

    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        params=querystring
    )

    decodedResponse = json.loads(response.text)
    print(json.dumps(decodedResponse, sort_keys=True, indent=4))


if __name__ == '__main__':
    args = get_args()
    ip_address = args.ip_address
    verbose = args.verbose
    check_abuse_ipdb()
