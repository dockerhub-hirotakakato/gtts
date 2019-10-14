FROM alpine:latest

RUN set -eux; \
    apk add --no-cache py3-flask py3-gunicorn; \
    pip3 install gTTS

COPY main.py /

CMD ["gunicorn", "-b=:80", "--access-logfile=-", "main:app"]
