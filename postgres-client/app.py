import logging
import os
import time

import psycopg2

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main():
    dsn = os.environ["DATABASE_URL"]
    while True:
        with psycopg2.connect(dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version()")
                version = cur.fetchone()[0]
                log.info("postgres: %s", version)
        time.sleep(10)


if __name__ == "__main__":
    main()
