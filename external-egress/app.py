import logging
import time

import requests

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

TARGETS = [
    "https://httpbin.org/get",
    "https://api.ipify.org?format=json",
]


def main():
    while True:
        for url in TARGETS:
            try:
                r = requests.get(url, timeout=10)
                log.info("GET %s → %d", url, r.status_code)
            except Exception as e:
                log.warning("GET %s failed: %s", url, e)
        time.sleep(30)


if __name__ == "__main__":
    main()
