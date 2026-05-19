FROM python:3.12-slim
WORKDIR /app
COPY worker.py .
RUN adduser --disabled-password --gecos '' appuser
USER appuser
CMD ["python", "worker.py"]
