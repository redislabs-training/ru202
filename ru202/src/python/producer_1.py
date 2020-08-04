'''
The simplest Natural Numbers (ISO 80000-2) Stream producer

Every run starts the count of numbers from zero
'''
from time import sleep, time
from util.connection import get_connection

if __name__ == '__main__':
    redis = get_connection()
    key = 'numbers'
    n = 0

    while True:
        # Obtain educational Stream growth statistics
        length = redis.xlen(key)
        usage = redis.memory_usage(key)
        print(f'{time():.3f}: Stream {key} has {length} messages and uses {usage} bytes')

        # Append the next message
        data = {'n': n}
        _id = redis.xadd(key, data)

        print(f'{time():.3f}: Produced the number {n} as message id {_id}')

        n += 1
        # Comment out the following line for non-educational use
        sleep(1)
