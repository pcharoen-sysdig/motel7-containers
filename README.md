# motel7-containers

Test containers for validating the motel7 internal PaaS platform. Each directory is a standalone scenario with its own `Dockerfile`.

## Scenarios

| Directory | What it is | What it validates |
|---|---|---|
| `simple-web/` | Minimal HTTP server with `/` and `/health` endpoints | Basic deployment, ALB ingress routing, health checks |
| `worker/` | Background process, no HTTP | Worker pod pattern (no ingress required) |
| `redis-client/` | Connects to Redis and increments a counter loop | `ManagedServiceProvisionWorkflow`, secret injection via env |
| `postgres-client/` | Runs `SELECT version()` against Postgres on a loop | DB managed service, `DATABASE_URL` secret injection |
| `slow-start/` | Returns HTTP 503 on `/health` for 45s, then 200 | Readiness probe patience, deployment status tracking |
| `crash-loop/` | Exits with code 1 after 10s | Restart policy behavior, platform alerting, lease failure handling |
| `privileged-rejected/` | Runs as root; includes `pod.yaml` requesting `privileged: true` | Kyverno `ClusterPolicy` + PSA enforcement at admission |
| `external-egress/` | Makes outbound HTTPS calls to public hosts every 30s | Egress proxy allowlist enforcement |
| `ubuntu-box/` | Ubuntu 24.04 with curl, dig, nmap, tcpdump, jq, etc. | General-purpose interactive debugging |

## Building

Each scenario builds independently from its directory:

```bash
docker build -t motel7-test/<scenario> ./<scenario>

# examples
docker build -t motel7-test/simple-web ./simple-web
docker build -t motel7-test/ubuntu-box ./ubuntu-box
```

## Deploying via motel7

Push images to your registry, then register them as an app via the motel7 web UI or API.

### Managed service scenarios

`redis-client` and `postgres-client` require provisioning the corresponding managed service first. The platform injects credentials as Kubernetes Secrets mapped to environment variables:

| Scenario | Required env vars |
|---|---|
| `redis-client` | `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD` |
| `postgres-client` | `DATABASE_URL` |

### `privileged-rejected`

Build and push the image, then apply `privileged-rejected/pod.yaml` to a motel7-managed namespace. Set the `namespace` field to your project namespace. The Kyverno `ClusterPolicy` should reject the pod at admission — verify with `kubectl describe pod privileged-test`.

### `ubuntu-box`

Runs `sleep infinity` by default. Once deployed, exec into the pod for interactive debugging:

```bash
kubectl exec -it <pod-name> -n <namespace> -- bash
```
