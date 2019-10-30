# ZimadTest
Test task for ZiMAD company

## Requirements
* Python 3
* PostgrezSQL
* RabbitMQ


## Installation
1. Enter the project dir
    ~~~
   cd ZimadTest
   ~~~
2. Create ZimadTest/db.json with database settings, for example
    ~~~
    {
      "ENGINE": "django.db.backends.postgresql_psycopg2",
      "NAME": "dbname",
      "USER": "username",
      "PASSWORD": "password",
      "HOST": "127.0.0.1",
      "PORT": 5432
    }
    ~~~

3. Create ZimadTest/rmq.json with RabbitMQ settings, for example
    ~~~
    {
      "username": "username",
      "password": "password",
      "host": "127.0.0.1",
      "port": 5672
    }
    ~~~
4. Install python virtual environment
    ~~~
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
    ~~~
5. Start the Django server
    ~~~
   python manage.py runserver 0.0.0.0:8000
   ~~~ 
6. Start the Celery worker
    ~~~
   celery -A ZimadTest worker -l info
   ~~~
   If you want to start the process in background,
   read the [Celery documentation](http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#daemonizing)
7. [Enjoy](http://127.0.0.1:8000)

## API endpoints
1. **/users/api/list/** - for list of users paginatet by 20 entries per page.
2. **/users/api/detail/USER_ID/** - for user detail (change USER_ID to user id).