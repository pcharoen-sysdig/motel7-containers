import logging
import os
import time

import redis

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main():
    r = redis.Redis(
        host=os.environ["REDIS_HOST"],
        port=int(os.environ.get("REDIS_PORT", 6379)),
        password=os.environ.get("REDIS_PASSWORD"),
        decode_responses=True,
    )
    while True:
        count = r.incr("test:counter")
        log.info("counter = %d", count)
        time.sleep(5)


if __name__ == "__main__":
    main()
