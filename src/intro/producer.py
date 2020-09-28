# Use Case: Streams example with Python
# Usage: Part of Redis University RU202 courseware
from redis import Redis
import random
import time
import json
import os

class Measurement:
    def __init__(self):
        self.postal_codes = [94016, 80014, 60659, 10011]
        self.current_temp = 50
        self.max_temp = 100
        self.min_temp = 0

    def get_next(self):
        if random.random() >= 0.5:
            if self.current_temp + 1 <= self.max_temp:
                self.current_temp += 1
        elif self.current_temp - 1 >= self.min_temp:
            self.current_temp -= 1

        return {'postal_code': self.postal_codes[0], 'temp_f': self.current_temp}

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
        client_kwargs["password"]

    redis = Redis(**client_kwargs)

    stream_key = "stream:weather"
    measurement = Measurement()

    while True:
        entry = measurement.get_next()
        id = redis.xadd(stream_key, entry, "*")
        print("Wrote " + json.dumps(entry) + " with ID " + id)
        time.sleep(1)

if __name__ == "__main__":
    main()
