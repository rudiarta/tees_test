FROM python:3.7.8-slim-stretch
RUN mkdir /app
WORKDIR /app
RUN apt update && apt install curl
EXPOSE 5000
CMD [ "tail", "-f", "/dev/null" ]