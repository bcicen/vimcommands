from alpine:3.2

RUN apk add --update python3 python3-dev gcc musl musl-dev && \
    rm -f /var/cache/apk/*

COPY . /app/

RUN pip3 install -r /app/requirements.txt

EXPOSE 8000
CMD python3 /app/api.py
