FROM python:3.7.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add gcc python3-dev musl-dev

COPY bot.py .
COPY cogs .
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "python", "bot.py"]
