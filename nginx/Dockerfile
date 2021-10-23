FROM ubuntu/nginx:latest


RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/


RUN apt-get -y upgrade
RUN apt install python3-certbot-nginx


