django-flatpages-i18n
=====================

Translatable version of django.contrib.flatpages with basic menu support.

Installation
-------------

```
$ pip install django-flatpages-i18n
```

Add new applications at the end of INSTALLED_APPS in your settings.py.

```python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'south',
    'modeltranslation',
    'flatpages_i18n',
)
```

Before the migration we need create the list of all available languages in settings.py.

```python
LANGUAGE_CODE = 'en'

from django.utils.translation import gettext

LANGUAGES = (
    ('de', gettext('German')),
    ('en', gettext('English')),
)
```
Don't forget to add an FlatpageFallbackMiddleware into MIDDLEWARE_CLASSES.

```python
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Don't forget
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'flatpages_i18n.middleware.FlatpageFallbackMiddleware'
)
```

Run the migrations.

```
$ python manage.py schemamigration flatpages_i18n --init
$ python manage.py migrate flatpages_i18n
```

{% load i18n flatpages %}

{% get_available_languages as LANGUAGES %}
{% get_flatpages_i18n as flatpages_i18n %}

Usage
------

templates/home.html

```
{% load i18n flatpages %}

{% get_available_languages as LANGUAGES %}
{% get_flatpages_i18n as flatpages_i18n %}

<ul>
    {% for flatpage in flatpages_i18n %}
        <li><a href="/{{ LANGUAGE_CODE }}{{ flatpage.url }}">{{ flatpage.title }}</a></li>
    {% endfor %}
</ul>
```

or by using simple menu system

```
<div id="navigation">
    {% get_menu %}
</div>
```

get only children of menu item identified by ID

```
<div id="navigation">
    {% get_menu 2 %}
</div>    
```
