FROM python:3.7.5-alpine3.10

COPY ./requeriments/requeriments_prod.txt /app/requeriments.txt

WORKDIR /app

RUN pip install -r requeriments.txt

COPY . /app

ENTRYPOINT [ "python" ]
CMD [ "src/run.py" ]
