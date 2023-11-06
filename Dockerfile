FROM python:3.7-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]



# Here first we created a base [ FROM python:3.7-slim-buster ] which is like saying we need to use the python 3.7 slim version based on buster
# ( which is a light weight version of python suitable for running files in docker container)

# then using run we first updated our local package index (RUN apt update -y) which is like the default packages and all
# it automatically contains like bash, git , mysql-server etc.. After that we install aswcli fro AWS pupose

# Then we creating a working directory called app, and then we copy everythin in the current working directory of our pc into app

# then we install requirements.txt
# and by using CMD it initially runs our previous app.py at first which is the starting point
