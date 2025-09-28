release: cd projeto && python manage.py collectstatic --noinput && python manage.py migrate
web: cd projeto && PYTHONPATH=/app/projeto:/app gunicorn base.wsgi --bind 0.0.0.0:$PORT