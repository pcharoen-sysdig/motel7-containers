FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN adduser --disabled-password --gecos '' appuser
USER appuser
CMD ["python", "app.py"]
