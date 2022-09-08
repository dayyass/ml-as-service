FROM python:3.7-slim-buster
MAINTAINER Dani El-Ayyass <dayyass@yandex.ru>
WORKDIR /app
COPY api.py gunicorn.conf.py inference.py requirements.txt ./

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# run gunicorn server
CMD ["gunicorn", "--config", "gunicorn.conf.py", "api:app"]
