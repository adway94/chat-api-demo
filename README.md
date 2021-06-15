PYTHON CHAT

## About this proyect

```
These proyects were made posible thanks to Alkemy labs
Know more: http://www.alkemy.org/
LinkedIn: https://www.linkedin.com/company/alkemy2020/
```

Install environment

```commandline
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
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
