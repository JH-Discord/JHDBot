FROM python:3.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY captcha.py .
COPY templates templates/

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "captcha.py"]
