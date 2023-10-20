FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
ADD . /web/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient
COPY . /web/


