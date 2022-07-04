FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir

COPY ./ /app

RUN chmod +x /app/entrypoint.sh

# CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD [ "run" ]

LABEL author='yasin.alizade@yandex.ru' version=1 broken_keyboards=500