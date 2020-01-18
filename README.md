# python101

Local :http://127.0.0.1:8000/tweet/

You can run with `python manage.py runserver`

## Starter

- install `https://www.anaconda.com/distribution/#download-section` (Python 2.7 version)

- `conda create -n django python=3.7`

- `conda activate django`

- `pip install Django`

- Create new project `django-admin startproject <your-project-name>`

- update dependency `pip install -r requirements.txt`

> If you have new dependency you can freeze your dependency by `pip freeze > requirements.txt` command.

## Migration

- python manage.py makemigrations tweet (add migration)

- python manage.py migrate (update your DB)

## Ref

ref: https://towardsdatascience.com/get-your-computer-ready-for-machine-learning-how-what-and-why-you-should-use-anaconda-miniconda-d213444f36d6

ref: https://www.djangoproject.com/download/

ref: https://www.django-rest-framework.org/

ref-test: https://docs.djangoproject.com/en/3.0/intro/tutorial05/#tests-will-save-you-time

ref-swagger: https://django-rest-swagger.readthedocs.io/en/latest/

ref-lib: https://www.reddit.com/r/django/comments/epooab/what_public_apps_do_you_use_with_mostall_of_your/
