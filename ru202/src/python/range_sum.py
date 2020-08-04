'''
Sum the numbers in the Stream with range queries and persist results
in a Hash as an optimization
'''
from util.connection import get_connection
from util.streams import incr_id

if __name__ == '__main__':
    redis = get_connection()

    key = 'numbers'
    sum_key = f'{key}:range_sum'
    n_count = 0

    # Load the previous state or initialize it
    h = redis.hgetall(sum_key)
    if not h:
        # Assume first run and initialize when the Hash does not exist
        last_id = '-'
        n_sum = 0
    else:
        last_id = h['last_id']
        n_sum = int(h['n_sum'])

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
            n_count += 1

        # Increment the last known ID for the next iteration
        last_id = incr_id(last_id)

    # Store the last known state and report it
    if n_count != 0:
        redis.hmset(sum_key, {
            'last_id': last_id,
            'n_sum': n_sum,
        })

    print(f'The running sum of the Natural Numbers Stream is {n_sum} (added {n_count} new numbers)')
