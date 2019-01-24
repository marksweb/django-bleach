#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='django-bleach',
    version="0.4.0",
    description='Easily use bleach with Django models and templates',
    long_description=long_description,
    author='Mark Walker',
    author_email='theshow@gmail.com',
    url='https://github.com/marksweb/django-bleach',
    packages=find_packages(),
    install_requires=[
        'bleach',
        'Django>=1.8',
    ],
    package_data={},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
    ],
)
