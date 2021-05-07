# Social-Network-django-
About project-
This is a basic social network website which is in development stage built on Django's. It has features like user's profile page, posts and groups page where you can add, update and delete posts and groups.

For Developers/Contributers: To Set up follow these steps -

Run on git terminal
 git clone https://github.com/sararamadanshater/Social-Network-django-
Change working directory to /Social-Network-django

1) make virtualenv
 - virtual env <env-name>
 
2) Activate your virtual environment
 - source env/bin/activate
 
3) Install requirements
 - pip install django 
 - pip intsall Pillow 
 - pip install django_crispy_forms 
 - pip install django_allauth 
 - pip install misaka 
 - pip install django-braces 
 
4) Run migrations :
 - python3 manage.py makemigrations
 - python3 manage.py migrate
 
5) Run server :
 - python3 manage.py runserver 
