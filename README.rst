django-flatpages-i18n
=====================

Translatable version of django.contrib.flatpages with menu support.


Requirements
------------
- Django
- django_modeltrans
- django_mptt
- django-pragmatic

Tested with Django 1.8.


Installation
-------------

1. Install python library using pip: ``pip install django-flatpages-i18n``

2. Add ``mptt``, ``modeltrans`` and ``flatpages_i18n`` to ``INSTALLED_APPS`` in your Django settings file

3. Migrate your database

4. Specify desired languages in your Django settings file::

    from django.utils.translation import gettext

    LANGUAGE_CODE = 'en'
    LANGUAGES = (
        ('en', gettext('English')),
        ('de', gettext('German')),
    )



5. Addd ``'flatpages_i18n.urls'`` to your urls.py::

    if 'flatpages_i18n' in settings.INSTALLED_APPS:
        urlpatterns += i18n_patterns(
            path(pgettext_lazy('url', 'pages/'), include('flatpages_i18n.urls')),
        )


Usage
-----

To get all flatpages:
'''''''''''''''''''''

In your HTML template::

    {% load i18n flatpages_i18n %}
    {% get_flatpages_i18n as flatpages_i18n %}

    <ul>
        {% for flatpage in flatpages_i18n %}
            <li><a href="{{ flatpage.get_absolute_url }}">{{ flatpage }}</a></li>
        {% endfor %}
    </ul>


To get flatpage by its PK::

    {% get_flatpage_i18n 123 as my_flatpage %}
    {{ my_flatpage.content_i18n }}


or by its machine_name::

    {% get_flatpage_i18n 'my-flatpage' as my_flatpage %}


Menu system:
''''''''''''

To print all menu items::

    <div id="navigation">
        {% menu_i18n %}
    </div>

to get only children of menu item identified by its PK::

    <div id="navigation">
        {% menu_i18n 2 %}
    </div>

or by its machine_name::

    <div id="navigation">
        {% menu_i18n 'footer-menu' %}
    </div>

You can also assign menu items into variable::

    {% get_menu_i18n 'my-menu' as my_menu %}
    {% for item in my_menu %}
        <a href="{{ item.get_absolute_url }}" target="{{ item.target }}">{{ item }}</a>
    {% endfor %}

Authors
-------

Library is by `Erik Telepovsky` from `Pragmatic Mates`_. See `our other libraries`_.

.. _Pragmatic Mates: http://www.pragmaticmates.com/
.. _our other libraries: https://github.com/PragmaticMates
