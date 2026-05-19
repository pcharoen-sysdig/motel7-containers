import logging
import os
import time
from urllib.parse import urlparse

import psycopg2

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def _redact_dsn(dsn):
    parsed = urlparse(dsn)
    if parsed.password:
        return dsn.replace(f":{parsed.password}@", ":***@")
    return dsn


def main():
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        log.error("DATABASE_URL is not set — cannot connect to Postgres")
        return
    log.info("DATABASE_URL = %s", _redact_dsn(dsn))
    while True:
        with psycopg2.connect(dsn) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version()")
                version = cur.fetchone()[0]
                log.info("postgres: %s", version)
        time.sleep(10)


if __name__ == "__main__":
    main()
