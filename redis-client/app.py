import logging
import os
import time

import redis

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main():
    host = os.environ.get("REDIS_HOST")
    if not host:
        log.error("REDIS_HOST is not set — cannot connect to Redis")
        return
    port = int(os.environ.get("REDIS_PORT", 6379))
    password = os.environ.get("REDIS_PASSWORD")
    log.info("REDIS_HOST = %s  REDIS_PORT = %s  REDIS_PASSWORD = %s", host, port, "set" if password else "not set")
    r = redis.Redis(
        host=host,
        port=port,
        password=password,
        decode_responses=True,
    )
    while True:
        count = r.incr("test:counter")
        log.info("counter = %d", count)
        time.sleep(5)


if __name__ == "__main__":
    main()
