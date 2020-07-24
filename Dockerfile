FROM nginx:latest

WORKDIR /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf

COPY verify-app.conf /etc/nginx/conf.d/

EXPOSE 80
