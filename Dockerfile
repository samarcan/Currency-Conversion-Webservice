FROM python:3.7.5-alpine3.10

COPY ./requeriments/requeriments_prod.txt /app/requeriments.txt

RUN pip install -r /app/requeriments.txt

COPY . /app

WORKDIR /app/src

ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
