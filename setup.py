#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-flatpages-i18n',
    version='2.0.2',
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
    install_requires=('django', 'django_modeltrans', 'django_mptt', 'markdown', 'martor', 'django-tinymce', 'django-pragmatic'),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License'],
    license='BSD License',
    keywords="django flatpages translation i18n",
)
