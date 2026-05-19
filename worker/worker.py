import logging
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main():
    count = 0
    while True:
        count += 1
        log.info("processing item %d", count)
        time.sleep(5)


if __name__ == "__main__":
    main()
