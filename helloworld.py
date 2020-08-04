"""Simple script to test connection to Redis and print an existing key."""
from redis import Redis
import os

redis = Redis(host=os.environ.get("REDIS_HOST", "localhost"),
              port=os.environ.get("REDIS_PORT", 6379),
              db=0)

print(redis.get("hello"))
