FROM python:3.6

RUN mkdir -p /app
WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

EXPOSE 8888

ENTRYPOINT ["python"]
CMD ["run.py"]