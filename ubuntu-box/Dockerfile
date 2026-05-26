# General-purpose debugging box. Runs as root intentionally for interactive use.
FROM ubuntu:24.04
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        wget \
        dnsutils \
        iputils-ping \
        netcat-openbsd \
        nmap \
        telnet \
        tcpdump \
        net-tools \
        iproute2 \
        vim \
        jq \
        less \
        procps \
        ca-certificates \
        git \
        redis-tools \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
CMD ["bash", "-c", "echo '=== environment variables ===' && env | sort && echo '=== end ===' && sleep infinity"]
