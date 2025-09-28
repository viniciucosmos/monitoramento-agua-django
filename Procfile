release: python manage.py collectstatic --noinput && python manage.py migrate
web: gunicorn base.wsgi --bind 0.0.0.0:$PORT