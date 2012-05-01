#!/usr/bin/env python

try:
	from setuptools import setup, find_packages
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, find_packages

setup(
    name='django-bleach',
    version="0.1.0",
    description='Easily use bleach with Django models and templates',
    author='Tim Heap',
    author_email='heap.tim@gmail.com',
    url='https://bitbucket.org/ionata/django-bleach',
    packages=['django_bleach',],
    install_requires = ['bleach'],
    package_data={},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

