FROM alpine:3.12

RUN apk add --update --no-cache \
    gcc \
    alpine-sdk \
    linux-headers \
    python3 \
    python3-dev \
    py3-pip \
    libffi-dev \
    build-base

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn gevent

RUN adduser -D gunicorn
USER gunicorn

EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--access-logfile", "-", "captcha:app", "-k", "gevent", "--worker-connections", "1000"]
