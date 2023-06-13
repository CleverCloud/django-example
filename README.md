# Clever Coud Django project

This project allows you to quickly begin a Django project on Clever Cloud.

## Pre-requisites

- A working version of Python. This project has been tested on Python 3.6+.
- At least one Nano instance (Pico doesn't have enough resources for a Django project)
- Postgresql version 12 if you're using django 4.2+ (postgresql 11 is deprecated since this version)

### Database

By default, Django will use a local sqlite database that won't persist between deployments. So you need to choose a non-local technology.

Django supports [some DBs](https://docs.djangoproject.com/en/2.1/ref/settings/#databases) and Clever Cloud can host somes as [add-ons](https://www.clever-cloud.com/doc/addons/).
To keep it simple, you can run it either on MySQL or PostgreSQL. This project will choose to run with PostgreSQL.

For local work, you can grab [PostgreSQL](https://www.postgresql.org/download/) easily; or [MySQL](https://dev.mysql.com/downloads/) and its compatible alternative [MariaDB](https://downloads.mariadb.org/).

## Project creation

First you need to [fork](https://help.github.com/articles/fork-a-repo/) the project or [duplicate it](https://help.github.com/articles/duplicating-a-repository/).

Then, if you chose to run with MySQL instead of PostgreSQL, adapt the `DATABASES` configuration in `cc_django/settings.py`.

## Clever Tools connect

This tutorial will use the [Clever Tools ClI](https://www.clever-cloud.com/doc/clever-tools/getting_started/).

It will allow you to create, configure and deploy your application on Clever Cloud from console.

In the following steps, we will suppose that you name (adapt to your needs) in the Clever Cloud dashboard :

* your application : `django-cc` 
* your corresponding database add-on : `django-cc-pc`

### Create the app and add-on

At the root of the project :

```bash
clever login
```

Log in the UI and close it. Then create your Python application and PostgreSQL add-on :

```bash
clever create --type python --region par django-cc
clever addon create --region eu --plan dev --link django-cc postgresql-addon django-cc-pg
```

More information on parameters [HERE](https://www.clever-cloud.com/doc/clever-tools/create/).

If needed, you can set the scaling :

```bash
clever scale --min-flavor pico --max-flavor pico
clever scale --min-instances 1 --max-instances 1
```

More information on scaling [HERE](https://www.clever-cloud.com/doc/clever-tools/manage/).

### Environment setup

You need to setup some Environment variables accordingly to your `settings.py` :

```bash
clever env set PYTHON_VERSION "3.6"
clever env set STATIC_FILES_PATH "static/"
clever env set STATIC_URL_PREFIX "/static"
clever env set PYTHON_BACKEND "uwsgi"
```

More information on Python environement variables [HERE](https://www.clever-cloud.com/doc/python/python_apps/).

### Deploy !

Nothing else left to do, just go on and deploy your app :

```bash
clever deploy
```

Note :

If deployement failed with some error like : 

```bash
django.db.utils.OperationalError: could not translate host name "XXXXXXXXXX-postgresql.services.clever-cloud.com" to address: Name or service not known
```

It only means that you deployed too quickly after creating the PG add-on and name propagation has not yet been done. Wait a bit and try again later.

### URL

Your application automatically has a domain pointing to it. You can obtain it though :

```bash
clever domain
```

To add other domains, more information [HERE](https://www.clever-cloud.com/doc/admin-console/custom-domain-names/).
