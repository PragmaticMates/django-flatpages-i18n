django-flatpages-i18n
=====================

Translatable version of django.contrib.flatpages with basic menu support.


Requirements
------------
- Django
- django_modeltranslation
- django_mptt

Tested with Django 1.8.


Installation
-------------

1. Install python library using pip: ``pip install django-flatpages-i18n``

2. Add ``mptt``, ``modeltranslation`` and ``flatpages_i18n`` to ``INSTALLED_APPS`` in your Django settings file

3. Add ``flatpages_i18n.middleware.FlatpageFallbackMiddleware`` to ``MIDDLEWARE_CLASSES`` in your Django settings file

4. Specify desired languages in your Django settings file::

    from django.utils.translation import gettext

    LANGUAGE_CODE = 'en'
    LANGUAGES = (
        ('en', gettext('English')),
        ('de', gettext('German')),
    )

5. Migrate your database

6. Run ``sync_translation_fields`` and ``update_translation_fields`` commands (from ``modeltranslation`` app)

7. If you want to use Redactor WYSIWYG editor (see settings below), you need to add ``'flatpages_i18n.urls'`` to your urls.py::

    if 'flatpages_i18n' in settings.INSTALLED_APPS:
        urlpatterns += i18n_patterns('',
            url(r'^', include('flatpages_i18n.urls')),
        )


Usage
-----

To get all flatpages:
'''''''''''''''''''''

In your HTML template::

    {% load i18n flatpages_i18n %}

    {% get_available_languages as LANGUAGES %}
    {% get_flatpages_i18n as flatpages_i18n %}

    <ul>
        {% for flatpage in flatpages_i18n %}
            <li><a href="/{{ LANGUAGE_CODE }}{{ flatpage.url }}">{{ flatpage.title }}</a></li>
        {% endfor %}
    </ul>


To get flatpage by its PK::

    {% get_flatpage_i18n 123 as my_flatpage %}
    {{ my_flatpage.content }}


or by its machine_name::

    {% get_flatpage_i18n 'my-flatpage' as my_flatpage %}


Menu system:
''''''''''''

To print all menu items::

    <div id="navigation">
        {% get_menu %}
    </div>


to get only children of menu item identified by its PK::

    <div id="navigation">
        {% get_menu 2 %}
    </div>

or by its machine_name::

    <div id="navigation">
        {% get_menu 'footer-menu' %}
    </div>


Settings
--------

FLATPAGES_EDITOR
    If you wish to use `Redactor`_ as WYSIWYG editor, set it to ``'REDACTOR'``. Default: ``None``.

FLATPAGES_REDACTOR_JS
    Path to Redactor .js file. Default: ``'js/redactor/redactor.js'``.

FLATPAGES_REDACTOR_CSS
    Path to Redactor .css file. Default: ``'css/redactor/redactor.css'``.


Authors
-------

Library is by `Erik Telepovsky` from `Pragmatic Mates`_. See `our other libraries`_.

.. _Pragmatic Mates: http://www.pragmaticmates.com/
.. _our other libraries: https://github.com/PragmaticMates
.. _Redactor: http://imperavi.com/redactor/
