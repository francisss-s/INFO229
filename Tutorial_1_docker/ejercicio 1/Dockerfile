FROM python:3.9.1

ENV SLACK_TOKEN="xoxb-1419412195043-1488045592838-BpGrF8np6BuJqoJxazJkRbga"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./jamesbot.py /jamesbot.py
COPY ./jamesbot_app.py /jamesbot_app.py

CMD [ "python", "/jamesbot_app.py" ]