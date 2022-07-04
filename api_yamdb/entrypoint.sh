#!/bin/sh

if [ -z "$1" ]
    then
    echo "no argument supplied"
    exit 1
elif [ $1 = 'migrate' ]
    then
        python manage.py migrate
        python manage.py load_users_data
        python manage.py load_all_data
elif [ $1 = 'pre-run' ]
    then
        python manage.py collectstatic --noinput
elif [ $1 = 'run' ]
    then
        exec $(which gunicorn) api_yamdb.wsgi:application --bind=0:9010
        exit $?
else
    echo "Invalid argument"
    exit 1
fi
