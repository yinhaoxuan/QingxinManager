sudo fuser -k 8000/tcp
gunicorn QingxinManager.wsgi -b 0:8000 &
