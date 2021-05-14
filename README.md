PYTHON CHAT

## About this proyect

```
These proyects were made posible thanks to Alkemy labs
Know more: http://www.alkemy.org/
LinkedIn: https://www.linkedin.com/company/alkemy2020/
```


Install environment

```commandline
py -m venv env
.\env\Scripts\activate
py -m pip install requests
```

Create database and first user

```commandline
python manage.py migrate
python manage.py createsuperuser
```

Run testing server

```commandline
python manage.py runserver
```
