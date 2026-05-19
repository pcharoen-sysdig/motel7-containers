FROM python:3.12-slim
RUN pip install --no-cache-dir flask==3.1.0
WORKDIR /app
COPY app.py .
RUN adduser --disabled-password --gecos '' appuser
USER appuser
EXPOSE 8080
CMD ["python", "app.py"]
