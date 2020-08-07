FROM python:3.7.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add gcc python3-dev musl-dev

COPY bot.py .
COPY cogs .
COPY helpembed.py .
COPY webhook_logging webhook_logging
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install webhook_logging/.

CMD ["python", "bot.py"]
