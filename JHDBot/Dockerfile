# Builder image
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.7.8-alpine as builder

ARG TARGETPLATFORM

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

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

COPY requirements.txt   .

# Build python
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# Final image; no build dependencies so image is smaller
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.7.8-alpine

# Add non root user
RUN addgroup -S app && adduser app -S -G app

WORKDIR /home/app/

# Copy project files
COPY --from=builder /wheels ./wheels
COPY --from=builder /app/requirements.txt .

COPY bot.py             .
COPY cogs               .
COPY gifs               .

# Setup permissions and user path
RUN chown -R app /home/app && \
  mkdir -p /home/app/python && chown -R app /home/app
USER app
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python

# Install previously built python wheels
RUN pip install --no-cache /home/app/wheels/* --target=/home/app/python

HEALTHCHECK CMD discordhealthcheck || exit 1

CMD ["python", "bot.py"]
