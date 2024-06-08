FROM python:3.12

WORKDIR /project

ADD app/dumb_code.py .

RUN pip install psutil

CMD ["python", "./dumb_code.py"]