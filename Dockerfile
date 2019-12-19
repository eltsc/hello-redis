FROM python:3

WORKDIR /usr/src/app

RUN pip3 install Flask
RUN pip3 install redis

COPY ./web .

EXPOSE 8080

CMD [ "python3", "./web.py" ]