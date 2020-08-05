FROM nginx:latest

WORKDIR /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf .

EXPOSE 80
