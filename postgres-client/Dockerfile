FROM python:3.12-slim
RUN pip install --no-cache-dir psycopg2-binary==2.9.10
WORKDIR /app
COPY app.py .
RUN adduser --disabled-password --gecos '' appuser
USER appuser
CMD ["python", "app.py"]
