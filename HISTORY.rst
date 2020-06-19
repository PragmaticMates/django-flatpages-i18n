History
=========

0.1.3 (2013-10-11)

* flatpages are able to put into trees by using ``django-mptt`` application
* basic menu system support
* removed comment field for flatpages

0.2.0 (2014-01-17)
* refactored flatpages > flatpages_i18n, update your template tags
* menu can be called also by its machine_name

0.2.1 (2014-01-17)
* uniqueness of MenuItem's machine_name

0.2.2 (2014-02-28)
* Django 1.6 support

0.3.0 (2014-03-04)
* get_flatpage_i18n template tag, use migration.

0.4.0 (2014-05-20)
* Django 1.8 support

0.4.4 (2017-03-01)
* Python 3 support

0.5.0 (2017-03-02)
* translation fields are synced automatically after initial migration

0.6.0 (2017-05-15)
* target of menu items

0.7.0 (2017-05-22)
* language code added to absolute path of FlatPage_i18n model
* support for django-seo2 app

0.7.1 (2018-01-24)
* support for Django 1.11

0.7.2
* support for languages with hyphens

1.0.0 (2020-06-19)
* Complete refactoring of whole package.
* Dropped support for Python 2
* django-modeltrans replaced django-modeltranslations
* flatpage doesn't have parent relationship
* dropped middleware, using urls instead
* dropped machine name for menu items
* dropped support for redactor editor
* GIN indexes
* WARNING: migrations are not compatible with versions < 1.0.0 !