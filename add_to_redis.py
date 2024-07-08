#!/usr/bin/env python3
import csv
import redis


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_SET_NAME = 'ip_addresses'

CSV_FILE_PATH = 'ipv4.csv'


def connect_to_redis():
    """Establish a connection to Redis."""
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def add_ips_to_redis():
    """Read IP addresses from CSV and add them to a Redis set."""
    r = connect_to_redis()

    with open(CSV_FILE_PATH, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ip_address = row['IP']
            r.sadd(REDIS_SET_NAME, ip_address)

    return r.scard(REDIS_SET_NAME)


def main():
    set_size = add_ips_to_redis()
    print('IP addresses have been added to the Redis set.')
    print(f'Total number of unique IP addresses in the set: {set_size}')


if __name__ == '__main__':
    main()
