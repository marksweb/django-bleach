#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-bleach',
    version="0.3.0",
    description='Easily use bleach with Django models and templates',
    author='Mark Walker',
    author_email='theshow@gmail.com',
    url='https://bitbucket.org/marksweb/django-bleach',
    packages=find_packages(),
    install_requires=[
        'bleach',
        'Django>=1.8',
    ],
    package_data={},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
