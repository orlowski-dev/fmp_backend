FROM python:3

WORKDIR /usr/src/fmp_backend

RUN /bin/rm -rf /usr/src/fmp_backend/*

COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

COPY . .

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
