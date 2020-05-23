FROM alpine:3.7
MAINTAINER One Awesome Dev

ENV HOST="0.0.0.0" PORT="80" URL="http://127.0.0.1:5000"

RUN apk add --no-cache python3 py3-gevent py3-gunicorn && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN mkdir -p /opt/app
COPY ./tiny-flask/ /opt/app/
RUN pip3 install -qe /opt/app/

CMD gunicorn manage:app -b $HOST:$PORT --workers 3 -k gevent
