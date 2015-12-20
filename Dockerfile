from alpine:3.2

RUN apk add --update python3 python3-dev gcc musl musl-dev && \
    rm -f /var/cache/apk/*

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY api.py /app/api.py

EXPOSE 8000
CMD python3 /app/api.py
