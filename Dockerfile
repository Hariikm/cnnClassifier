FROM python:3.7-slim-buster

RUN apt update -y && install aswcli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]