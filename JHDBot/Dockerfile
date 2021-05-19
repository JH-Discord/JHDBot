FROM python:3.7.8-alpine

RUN mkdir -p /usr/src/app
RUN mkdir /usr/src/app/gifs
WORKDIR /usr/src/app

RUN apk add --update --no-cache \
            gcc \
            python3-dev \
            libc-dev \
            linux-headers \
            musl-dev \
            libxml2-dev \
            libxml2 \
            libxslt-dev \
            libxslt

COPY bot.py .
COPY cogs .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
