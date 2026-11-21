FROM python:3.12-slim

WORKDIR /app

COPY server.py index.html ./
COPY images/ ./images/

EXPOSE 5000

CMD ["python", "server.py"]
