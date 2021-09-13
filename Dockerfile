FROM tiangolo/uwsgi-nginx-flask:python3.9


WORKDIR /app

COPY templates /app/templates
COPY static /app/static

ADD main.py /app
ADD auth.py /app
ADD app.py /app
ADD forms.py /app
ADD main.py /app
ADD models.py /app
ADD requirements.txt /app
RUN export FLASK_APP=main.py

RUN chmod 0777 -R /app
RUN pip install -r requirements.txt

RUN apt-get install -y libpq-dev && pip install psycopg2

VOLUME /app

ENV FLASK_APP=/app/main.py