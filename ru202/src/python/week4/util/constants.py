# Constant declarations shared between producer and consumer.

STREAM_KEY_BASE = "temps"

AGGREGATING_CONSUMER_STATE_KEY = "aggregating_consumer_state"
AVERAGES_CONSUMER_STATE_KEY = "averages_consumer_state"
AVERAGES_STREAM_KEY = f"{STREAM_KEY_BASE}:averages"