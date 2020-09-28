"""Simple script to test connection to Redis."""
from redis import Redis
import os

redis = Redis(host=os.environ.get("REDIS_HOST", "localhost"),
              port=os.environ.get("REDIS_PORT", 6379),
              db=0,
              decode_responses=True)

print(redis.ping())