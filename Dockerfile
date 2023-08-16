FROM python:3.11

WORKDIR /home/provident_page

COPY . /home/provident_page

RUN apt-get update -y && apt-get update \
    && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev

RUN apt-get install -y tzdata && cp /usr/share/zoneinfo/Mexico/General /etc/localtime

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt