#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-flatpages-i18n',
    version='0.1.0',
    description='Translatable flatpages',
    long_description=(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-flatpages-i18n',
    packages=['flatpages_i18n'],
    package_data={},
    requires=[
        'South',
        'django_modeltranslation',
        'django(>=1.3)'
    ],
    download_url='https://github.com/downloads/deschler/django-modeltranslation/django-modeltranslation-0.4.0-beta2.tar.gz',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License'],
    license='New BSD')