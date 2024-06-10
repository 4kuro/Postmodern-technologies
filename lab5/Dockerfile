FROM python:3.9

COPY app/main.py /app/main.py
COPY test/test.py /app/test.py

WORKDIR /app

CMD ["python", "test.py"]
