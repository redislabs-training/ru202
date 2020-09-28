"""
Comparison of stream and sorted set data storage in Redis.
"""
import sys
from util.connection import get_connection

STREAM_KEY = 'ru202:demo:stream'
SORTED_SET_KEY = 'ru202:demo:sortedset'

def setup():
    """ Setup Redis keys and remove any from prior runs. """
    redis = get_connection()
    redis.delete(STREAM_KEY)
    redis.delete(SORTED_SET_KEY)

def producer(num_to_add):
    """ Add a configurable number of messages to the stream. """
    print(f'Producing {num_to_add} items.')

    redis = get_connection()

    for n in range(1, num_to_add + 1):
        message = f'hello{n}'

        # Add to stream. n here is the identifier.
        redis.xadd(STREAM_KEY, {'m': message}, n)

        # Add to sorted set. n here is the score.
        redis.zadd(SORTED_SET_KEY, {message: n})

def memory_usage():
    """ Compare memory used by stream and sorted set. """
    redis = get_connection()

    stream_memory_usage = redis.memory_usage(STREAM_KEY, 0)
    sorted_set_memory_usage = redis.memory_usage(SORTED_SET_KEY, 0)

    print(f'Stream memory usage:     {stream_memory_usage}')
    print(f'Sorted set memory usage: {sorted_set_memory_usage}')
    print(f'Difference:              {sorted_set_memory_usage - stream_memory_usage}')

    diff = sorted_set_memory_usage / stream_memory_usage
    print(f'Sorted set bigger by:    {format(diff, ".2f")}x')

if __name__ == '__main__':
    setup()

    num_to_produce = 10000

    if len(sys.argv) == 2:
        try:
            num_to_produce = int(sys.argv[1])
        except ValueError:
            sys.exit(f'Usage {sys.argv[0]} <number of messages>')

    producer(num_to_produce)
    memory_usage()
