# python101

Local: http://127.0.0.1:8000

You can run with `run-loc.sh`

## First time to clone

- You must have conda and prepared environment.
- Update dependency `pip install -r requirements.txt`
- Run project with `python manage.py runserver`
- Root page http://127.0.0.1:8000/
- Get tweet list http://127.0.0.1:8000/tweets/

> Simple script for prepared `init.sh`

> Simple script for run `run-loc.sh`

## Starter 101

- Install [CONDA](https://www.anaconda.com/distribution/#download-section)

- Creat conda environment (VM) `conda create -n django python=3.7`

- Active your conda environment `conda activate django`

- Install Django on your environment `pip install Django`

- Create new project with admin `django-admin startproject <your-project-name>`

> If you have new dependency you can freeze your dependency by `pip freeze > requirements.txt` command.

## Migration 101

### Add migration

`python manage.py makemigrations <your-migration-name>`

### Update your DB

`python manage.py migrate`

## Ref

ref: https://towardsdatascience.com/get-your-computer-ready-for-machine-learning-how-what-and-why-you-should-use-anaconda-miniconda-d213444f36d6

ref: https://www.djangoproject.com/download/

ref: https://www.django-rest-framework.org/

ref-test: https://docs.djangoproject.com/en/3.0/intro/tutorial05/#tests-will-save-you-time

ref-swagger: https://django-rest-swagger.readthedocs.io/en/latest/

ref-lib: https://www.reddit.com/r/django/comments/epooab/what_public_apps_do_you_use_with_mostall_of_your/
