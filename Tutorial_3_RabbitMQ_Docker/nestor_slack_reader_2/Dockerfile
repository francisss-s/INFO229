FROM python:3.6.3

ENV SLACK_TOKEN             xoxb-1419412195043-1488045592838-BpGrF8np6BuJqoJxazJkRbga
ENV SLACK_SIGNING_SECRET    401961d11ac465bf6d172e7cb2cc21fe

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]