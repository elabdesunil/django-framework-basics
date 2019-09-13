# Django Basics
Django backend that will hold some products and the products will be displayed like items in an e-commerce website.


Install Django
`pip install django`

To create a django project
`django-admin startproject pyshop .`

To run server
- on linux and windows`python manage.py runserver`
- on mac `python3 manage.py runserver`

To add a new app
`python manage.py startapp products`

To create View function:
    View Function is a function that gets called by the django when user navigates
    to a certain page.
    
To automatically create table:
`python manage.py makemigrations`

To generate table:
`python manage.py migrate`

To create the first user or superuser
`python manage.py createsuperuser`