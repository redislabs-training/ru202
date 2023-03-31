"""Simple script to test connection to Redis and print an existing key."""
from redis import Redis
import os

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

redis.set("hello", "world")
print(redis.get("hello"))
