FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.7.8-alpine

ARG TARGETPLATFORM

# Install packages
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

# Add non root user
RUN addgroup -S app && adduser app -S -G app

WORKDIR /home/app/

# Copy project files
COPY bot.py             .
COPY requirements.txt   .
COPY cogs               .
COPY gifs               .


RUN chown -R app /home/app && \
  mkdir -p /home/app/python && chown -R app /home/app
USER app
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python

RUN pip install -r requirements.txt --target=/home/app/python --no-cache-dir

HEALTHCHECK CMD discordhealthcheck || exit 1

CMD ["python", "bot.py"]
