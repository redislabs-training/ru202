'''
Redis connection utilities
'''

import os
from redis import Redis

def get_connection(name=None):
    '''Returns an optionally-named connection to Redis'''
    HOST = os.environ.get("REDIS_HOST", "localhost")
    PORT = os.environ.get("REDIS_PORT", 6379)
    USERNAME = os.environ.get("REDIS_USER")
    PASSWORD = os.environ.get("REDIS_PASSWORD")

    client_kwargs = {
        "host": HOST,
        "port": PORT,
        "decode_responses": True
    }

    if USERNAME:
        client_kwargs["username"] = USERNAME

    if PASSWORD:
        client_kwargs["password"] = PASSWORD

    redis = Redis(**client_kwargs)

    if name is not None:
        redis.client_setname(name)
    return redis