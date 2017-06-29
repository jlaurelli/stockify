# stockify

## Overview

An experimentation in a [Page as a component](https://hackernoon.com/reconciling-djangos-mvc-templates-with-react-components-3aa986cf510a)
approach to React components that interact with a Django backend.

## Additional dependencies
```
- docker-compose
- redis
- postgresql
```

## Getting Started
```
docker-compose build
docker-compose up -d
docker-compose run web /usr/local/bin/python manage.py migrate
```

Navigate to `localhost`.
