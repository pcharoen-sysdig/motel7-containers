import logging
import os
import time

import psycopg2

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

REQUIRED = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"]


def main():
    missing = [v for v in REQUIRED if not os.environ.get(v)]
    if missing:
        for var in missing:
            log.error("%s is not set — cannot connect to Postgres", var)
        return

    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    port = int(os.environ.get("DB_PORT", 5432))

    log.info("DB_HOST = %s  DB_PORT = %s  DB_NAME = %s  DB_USER = %s  DB_PASSWORD = set", host, port, dbname, user)

    while True:
        with psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version()")
                version = cur.fetchone()[0]
                log.info("postgres: %s", version)
        time.sleep(10)


if __name__ == "__main__":
    main()
