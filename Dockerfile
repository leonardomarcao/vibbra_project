FROM python:3.8

# these packages are necessary for psycopg2
RUN apt-get update \
    && apt-get -y install --no-install-recommends libpq-dev gcc \
    && pip install psycopg2[binary]==2.9.3

RUN mkdir /code
WORKDIR /code

COPY requirements.txt setup.py tox.ini ./
RUN pip3 install -U pip==21.1.1
RUN pip3 install -r requirements.txt
RUN pip3 install -e .

COPY app app/
COPY migrations migrations/
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
