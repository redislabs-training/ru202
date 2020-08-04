'''
Sum the numbers in the Stream and block for new messages
'''

from util.connection import get_connection

if __name__ == '__main__':
    redis = get_connection()

    key = 'numbers'
    sum_key = f'{key}:blockingread_sum'
    timeout = 100
    retries = 0

    # Load the previous state or initialize it
    h = redis.hgetall(sum_key)
    if not h:
        # Assume first run and initialize when the Hash does not exist
        last_id = '0-0'
        n_sum = 0
    else:
        last_id = h['last_id']
        n_sum = int(h['n_sum'])

    while True:
        # Get the next message
        reply = redis.xread({key: last_id}, count=1, block=timeout)

        # An empty response means we've timed out
        if not reply:
            # Try an exponential backoff
            if retries == 5:
                # Provide an alert and quit
                print('Waited long enough - bye bye...')
                break
            retries += 1
            timeout *= 2
            print(f'Retry #{retries}, timeout set to {timeout} milliseconds')
            continue

        # Process the messages
        for stream, messages in reply:
            for message in messages:
                last_id = message[0]
                n_sum += int(message[1]['n'])

        # Reset timeout and retries
        timeout = 100
        retries = 0

        # Store the last known state, if any work was done, and report it
        redis.hmset(sum_key, {
            'last_id': last_id,
            'n_sum': n_sum,
        })
        print(f'The running **blocking** read sum of the Natural Numbers Stream is {n_sum}')
