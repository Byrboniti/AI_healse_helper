FROM python:3.11

WORKDIR /usr/src/app
COPY ./sources/buy_proxy .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt