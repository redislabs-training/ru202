'''
Sum the numbers in the Stream with range queries
'''

from util.connection import get_connection
from util.streams import incr_id

if __name__ == '__main__':
    redis = get_connection()
    key = 'numbers'
    last_id = '0-1'  # The lowest valid full message ID in a Stream
    n_sum = 0

    while True:
        # Get the next batch of messages
        msgs = redis.xrange(key, min=last_id, max='+', count=5)

        # An empty response means we've exhausted the Stream
        if not msgs:
            break

        # Process each message in the bulk
        for msg in msgs:
            last_id = msg[0]
            n_sum += int(msg[1]['n'])

        # Increment the last known ID for the next iteration
        last_id = incr_id(last_id)

    print(f'The sum of the Natural Numbers Stream is {n_sum}')
