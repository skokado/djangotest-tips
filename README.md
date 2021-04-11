# Version

- Python: 3.8+
- Django: 3.2(LTS)
- pipenv: 2020.11.15
- PostgreSQL: 13.2

# Setup

```shell
$ git clone https://github.com/skokado/djangotest-tips.git
$ cd djangotest-tips
$ pipenv install --dev
$ pipenv shell

$ # Run database container
(djangotest-tips)$ docker run -d --rm --name django-db -p 5432:5432 -e POSTGRES_DB=django -e POSTGRES_USER=django -e POSTGRES_PASSWORD=django postgres:13.2

$ # Database Migration
(djangotest-tips)$ python3 manage.py makemigrations
(djangotest-tips)$ python3 manage.py migrate

$ # Start application
(djangotest-tips)$ DEBUG=1 python3 manage.py runserver 0:8000
```
