import logging
import sys
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

UPTIME_SECONDS = 10

if __name__ == "__main__":
    log.info("crash-loop container started, will exit in %ds", UPTIME_SECONDS)
    time.sleep(UPTIME_SECONDS)
    log.error("simulated crash — exiting with code 1")
    sys.exit(1)
