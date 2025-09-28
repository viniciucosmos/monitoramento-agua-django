release: python projeto/manage.py collectstatic --noinput && python projeto/manage.py migrate
web: gunicorn projeto.base.wsgi --bind 0.0.0.0:$PORT