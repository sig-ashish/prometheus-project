FROM python:3.7-alpine as prod

RUN apk add --update gcc libc-dev linux-headers && rm -rf /var/cache/apk/*
RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/

CMD ["python3", "pod_info.py"]
