FROM python:3.7.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add gcc \
            python3-dev \
            musl-dev \
            libxml2-dev \
            libxslt-dev

COPY bot.py .
COPY cogs .
COPY helpembed.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
