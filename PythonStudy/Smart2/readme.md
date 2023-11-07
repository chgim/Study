python -m venv venv
venv\Scripts\activate
pip install djangorestframework
pip install markdown
pip install django-filter
pip freeze > requirements.txt
venv\Scripts\django-admin startproject smart
cd smart
python manage.py runserver
python manage.py startapp board
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
admin / admin@admin.com / admin
