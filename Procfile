release: cd projeto && python manage.py collectstatic --noinput && python manage.py migrate
web: cd projeto && gunicorn base.wsgi --bind 0.0.0.0:$PORT