'''
Sum the numbers in the Stream with range queries, but backwards
'''
from util.connection import get_connection
from util.streams import decr_id

if __name__ == '__main__':
    redis = get_connection()
    key = 'numbers'
    last_id = '+'  # The special ID that means the last message in the Stream
    n_sum = 0

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

        # Decrement the last known ID for the next iteration
        last_id = decr_id(last_id)

    print(f'The **reverse sum** of the Natural Numbers Stream is still {n_sum}')
