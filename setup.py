#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-flatpages-i18n',
    version='0.1.0',
    description='Translatable flatpages',
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-flatpages-i18n',
    packages=find_packages(),
    install_requires=('South', 'django_modeltranslation', 'django'),
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
