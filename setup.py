#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='django-bleach',
    version="0.1.3",
    description='Easily use bleach with Django models and templates',
    author='Tim Heap',
    author_email='heap.tim@gmail.com',
    url='https://bitbucket.org/ionata/django-bleach',
    packages=find_packages(),
    install_requires=[
        'bleach',
        'Django>=1.3',
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
