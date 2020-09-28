'''
Sum the last N numbers in the Stream

Expects a single numeric argument as input, it being N.

Usage:
$ python range_3.py 10
'''

import sys
from util.connection import get_connection
from util.streams import decr_id

if __name__ == '__main__':
    redis = get_connection()
    N = int(sys.argv[1])  # Sum last N numbers

    key = 'numbers'
    last_id = '+'
    n_sum = 0
    n_count = 0

    while True:
        # Get the next batch of messages
        msgs = redis.xrevrange(key, max=last_id, min='-', count=5)

        # An empty response means we've exhausted the Stream
        if not msgs:
            break

        # Process each message in the bulk
        for msg in msgs:
            last_id = msg[0]
            n_sum += int(msg[1]['n'])
            n_count += 1
            if n_count == N:
                break

        if n_count == N:
            break

        # Increment the last known ID for the next iteration
        last_id = decr_id(last_id)

    print(f'The sum of the last {n_count} Natural Numbers in the Stream is {n_sum}')
    