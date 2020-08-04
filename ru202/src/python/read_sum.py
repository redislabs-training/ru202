'''
Sum the numbers in the Stream with read queries and persist results
in a Hash as an optimization
'''
from util.connection import get_connection

if __name__ == '__main__':
    redis = get_connection()

    key = 'numbers'
    sum_key = f'{key}:read_sum'
    n_count = 0

    # Load the previous state or initialize it
    h = redis.hgetall(sum_key)
    if not h:
        # Assume first run and initialize when the Hash does not exist
        last_id = '0-1'
        n_sum = 0
    else:
        last_id = h['last_id']
        n_sum = int(h['n_sum'])

    streamDict = {}

    while True:
        # Get the next batch of messages
        streamDict[key] = last_id
        msgs = redis.xread(streamDict, count=5)

        # An empty response means we've exhausted the Stream
        if not msgs:
            break

        # Process each message in the bulk
        # msgs[0] contains all the messages for the stream requested
        for msg in msgs[0][1]:
            last_id = msg[0]
            n_sum += int(msg[1]['n'])
            n_count += 1

    # Store the last known state and report it
    if n_count != 0:
        redis.hmset(sum_key, {
            'last_id': last_id,
            'n_sum': n_sum,
        })

    print(f'The running **read** sum of the Natural Numbers Stream is {n_sum} (added {n_count} new numbers)')
