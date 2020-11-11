# Use Case: Streams example with Python
# Usage: Part of Redis University RU202 courseware
import sys
import time
import json
import socket
import os
from redis import Redis
from redis.exceptions import ResponseError

def write_to_data_warehouse(results):
    if len(results) > 0:
        print("Wrote " + json.dumps(results) + " to data warehouse.\n")

def main():
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

    stream_key = "stream:weather"
    group_name = "data_warehouse_writer"
    consumer_name = "consumer-" + socket.gethostname() + "-a"
    block_ms = 5000
    stream_offsets = {stream_key: ">"}

    if not redis.exists(stream_key):
        print(f"Stream {stream_key} does not exist.  Try running the producer first.")
        sys.exit(0)

    try:
        redis.xgroup_create(stream_key, group_name)
    except ResponseError:
        print("Group already exists.")

    while True:
        results = redis.xreadgroup(group_name, consumer_name, stream_offsets, None, block_ms)
        write_to_data_warehouse(results)
        time.sleep(1)

if __name__ == "__main__":
    main()
