FROM python:3.7

COPY . /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN apt-get update && \
    apt-get install -y apt-utils binutils libproj-dev gdal-bin npm
RUN npm install -g yarn

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000