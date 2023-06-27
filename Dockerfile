FROM python:3.9

ENV DEBUG=False
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/django_sm_home

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/django_sm_home/

EXPOSE 8000

RUN [ "python", "manage.py", "migrate" ]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

