FROM python:3.9.1

ENV MONGO_PORT "mongodb://mongo:27017/"
ENV MONGO_HOST localhost
ENV SLACK_TOKEN="xoxb-1419412195043-1488045592838-BpGrF8np6BuJqoJxazJkRbga"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR ./app

COPY ./lalabot.py /lalabot.py
COPY ./lalabot_app.py /lalabot_app.py

CMD [ "python", "/lalabot_app.py" ]