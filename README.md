# stockify

## Additional dependencies
```
- docker-compose
- docker-machine
- redis
- postgresql
```

## Getting Started
```
docker-machine create -d virtualbox dev;
eval $(docker-machine env dev)
docker-compose build
docker-compose up -d
docker-compose run web /usr/local/bin/python manage.py migrate
```

Grab the associated IP address:
```
docker-machine ip dev
```

Navigate to that IP address.
