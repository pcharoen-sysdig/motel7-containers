# Intentionally runs as root with no USER instruction.
# Deploy with pod.yaml to verify Kyverno ClusterPolicy and PSA reject it at admission.
FROM ubuntu:24.04
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
CMD ["bash", "-c", "echo 'running as uid:' $(id -u) && sleep infinity"]
