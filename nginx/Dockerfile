FROM ubuntu/nginx:latest


RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/


RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN pip3 install certbot certbot-nginx



