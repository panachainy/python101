# python101

Local: http://127.0.0.1:8000

You can run with `run-loc.sh`

## Endpoint

- http://127.0.0.1:8000/admin
- http://127.0.0.1:8000/api/token/
- http://127.0.0.1:8000/api/token/refresh/
- http://127.0.0.1:8000/tweets
- http://127.0.0.1:8000/api/token/refresh/
- http://127.0.0.1:8000/api/token/refresh/

## First time to cloneƒ

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

### Create an admin user

`python manage.py createsuperuser`

### Set PostgreSQL into Settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your-database-name>',
        'USER': '<your-database-username>',
        'PASSWORD': '<your-database-password>',
        'HOST': '<your-database-host>',
        'PORT': '<your-database-port>',
    }
}
```

### Django Rest Framework

- Install our package requirements

`pip install djangorestframework`

`pip install pygments`

- Add INSTALLED_APPS

```json
(INSTALLED_APPS = ["rest_framework"])
```

## VENV

cd path to your project.

Create venv on your project `python3 -m venv <folder-name>`

Activate venv environment `source <folder-name>/bin/activate`

### Command

Check your dependency `pip list`

Exit current venv `deactivate`

Delete your venv `rm -rf <folder-name>`

Init your venv `python3 -m venv <folder-name> --system-site-packages`

### Set Environment Variable

Step:

- Connect your environment

  `conda activate your-env`

- Can update environment config in file environment.sh

- Run environment config into your environment


    Sqlite

    `run environment.sh`

    Postgres

    `run environment.sh postgres`

- Reactivate environment

  `conda deactivate`

  `conda actiavte your-env`

## Info

- Status code https://www.django-rest-framework.org/api-guide/status-codes

## Ref

ref: https://towardsdatascience.com/get-your-computer-ready-for-machine-learning-how-what-and-why-you-should-use-anaconda-miniconda-d213444f36d6

ref: https://www.djangoproject.com/download/

ref: https://www.django-rest-framework.org/

ref-test: https://docs.djangoproject.com/en/3.0/intro/tutorial05/#tests-will-save-you-time

ref-swagger: https://django-rest-swagger.readthedocs.io/en/latest/

ref-lib: https://www.reddit.com/r/django/comments/epooab/what_public_apps_do_you_use_with_mostall_of_your/

ref-django-test: https://www.youtube.com/watch?v=AKqd46cexzQ

ref-venv-mac: https://www.youtube.com/watch?v=Kg1Yvry_Ydk
