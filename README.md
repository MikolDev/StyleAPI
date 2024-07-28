# Style API

API created for fake online shops

## Technology

API was created with Django and REST framework. Python 3.12.0

## Getting started

0. After cloning repository go to `settings.py` and choose `DATABASE` configuration.

### Docker

1. Build and start containers

```
docker-compose build
docker-compose up
```

2. Apply database migrations

```
docker-compose exec web python manage.py migrate
```

3. Create superuser

```
docker-compose exec web python manage.py createsuperuser
```

### Alternatively

1. Make and activate your virtual environment.

2. Install requirements:

```
pip install -r requirements.txt
```

3. Run server:

```
python manage.py runserver
```

## Endpoints

All categories - post supported

```
/api/categories/
```

Category details - update and delete supported

```
/api/categories/<id>
```

All products - post supported

```
/api/products/
```

Product details - update and delete supported

```
/api/products/<id>
```

## Filters

Get all products from given category

```
/api/products/?category=<id>
```
