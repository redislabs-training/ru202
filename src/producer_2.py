'''
Every run starts the count from zero and stops after the one hundred and
first-th number (being one hundred).
IMPORTANT: The key is deleted before the main loop to recreate the stream.
'''
from time import time
from util.connection import get_connection

if __name__ == '__main__':
    redis = get_connection()
    key = 'numbers'
    n = 0
    m = 101
    redis.delete(key)  # NOT PRODUCTION CODE

    while n < m:
        data = {'n': n}
        _id = redis.xadd(key, data)

        print(f'{time():.3f}: Produced the number {n} as message id {_id}')

        n += 1
        