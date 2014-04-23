#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-flatpages-i18n',
    version='0.4.1',
    description='Translatable flatpages',
    long_description=open('README.rst').read(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-flatpages-i18n',
    packages=[
        'flatpages_i18n',
        'flatpages_i18n.templatetags',
        'flatpages_i18n.migrations'
    ],
    include_package_data=True,
    install_requires=('South', 'django_modeltranslation', 'django', 'django_mptt'),
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
    license='BSD License',
    keywords = "django flatpages translation i18n wysiwyg",
)
