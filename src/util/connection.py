'''
Redis connection utilities
'''

import os
from redis import Redis

def get_connection(name=None):
    '''Returns an optionally-named connection to Redis'''
    redis = Redis(host=os.environ.get("REDIS_HOST", "localhost"),
                  port=os.environ.get("REDIS_PORT", 6379),
                  db=0,
                  decode_responses=True)
    if name is not None:
        redis.client_setname(name)
    return redis