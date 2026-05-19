FROM python:3.12-slim
RUN pip install --no-cache-dir redis==5.2.1
WORKDIR /app
COPY app.py .
RUN adduser --disabled-password --gecos '' appuser
USER appuser
CMD ["python", "app.py"]
