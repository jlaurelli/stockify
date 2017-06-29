#!/bin/sh
cd /app/static
npm run build
cd ../..
python /app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn stockify.wsgi:application -w 2 -b :8000
