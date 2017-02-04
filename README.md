# BasicSite
minimal site to contain EternalDraft app

This project is the result of following the setup steps in EternalDraft (https://github.com/AlmostMatt/EternalDraft/blob/master/README.md)


pip install django-bootstrap3 (https://django-bootstrap3.readthedocs.io/en/latest/installation.html)

cd to directory that will contain the site
django-admin startproject almostmatt .
git submodule add https://github.com/AlmostMatt/EternalDraft.git

add 'EternalDraft', and 'bootstrap3', to settings.py INSTALLED_APPS
add url(r'^eternal/', include('EternalDraft.urls')), to almostmatt/urls.py

python manage.py migrate

python manage.py runserver

127.0.0.1:8000/eternal/
