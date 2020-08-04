'''
An example of concurrent consumers of the Natural Numbers Stream

The producer and consumers are implemented as subprocesses to simplify
the example's execution
'''

from multiprocessing import Process
from util.connection import get_connection

KEY = 'numbers'

def setup():
    ''' Initializes the Stream '''
    redis = get_connection()
    redis.delete(KEY)

def producer_func():
    ''' Natural Numbers Stream producer '''
    redis = get_connection()
    n = 0
    while n < 8:
        data = {'n': n}
        _id = redis.xadd(KEY, data)
        print(f'PRODUCER: Produced the number {n}')
        n += 1

    print('PRODUCER: No more numbers for you!')

def consumer_func(divisor):
    ''' Checks whether a number is divisible by the divisor without remainder '''
    redis = get_connection()
    timeout = 100
    retries = 0
    last_id = '$'

    while True:
        reply = redis.xread({KEY: last_id}, count=1, block=timeout)
        if not reply:
            if retries == 5:
                print(f'CONSUMER: Waited long enough for {divisor}s - bye bye...')
                break
            retries += 1
            timeout *= 2
            continue

        timeout = 100
        retries = 0

        # Process the messages
        for _, messages in reply:
            for message in messages:
                last_id = message[0]
                n = int(message[1]['n'])
                if n % divisor == 0:
                    print(f'CONSUMER: The number {n} can be divided by {divisor}')

if __name__ == '__main__':
    setup()
    consumer_of_twos = Process(target=consumer_func, args=(2, ))
    consumer_of_twos.start()
    consumer_of_threes = Process(target=consumer_func, args=(3, ))
    consumer_of_threes.start()
    producer = Process(target=producer_func)
    producer.start()
    