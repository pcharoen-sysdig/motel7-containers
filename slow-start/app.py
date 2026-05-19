import logging
import threading
import time

from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

STARTUP_DELAY = 45

app = Flask(__name__)
_ready = False


@app.route("/health")
def health():
    if _ready:
        return jsonify({"status": "ok"})
    return jsonify({"status": "starting"}), 503


@app.route("/")
def index():
    return jsonify({"message": "slow-start running", "ready": _ready})


def _finish_startup():
    global _ready
    log.info("simulating slow startup — sleeping %ds", STARTUP_DELAY)
    time.sleep(STARTUP_DELAY)
    _ready = True
    log.info("startup complete, /health now returns 200")


if __name__ == "__main__":
    threading.Thread(target=_finish_startup, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
