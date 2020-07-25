FROM python:3.7.8-slim-stretch
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt update && \
    apt install curl -y && \
    apt install build-essential -y
RUN make install-dependency
RUN rm -rf migrations
RUN make init
RUN make migrate
EXPOSE 8080
CMD [ "make", "run" ]