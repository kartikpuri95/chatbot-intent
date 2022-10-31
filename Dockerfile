FROM --platform=linux/amd64 python:3.7.10-stretch
WORKDIR /app
ADD . /app/
RUN apt-get update
RUN apt-get install -y libxmlsec1 pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl --allow-unauthenticated
RUN pip install --upgrade pip
RUN pip install gunicorn gunicorn['eventlet']
RUN pip install snips-nlu
RUN python -m snips_nlu download en

RUN pip install -r docker-requirements.txt
EXPOSE 5000

RUN pip install debugpy

RUN pip install gunicorn

CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "app:app"]
