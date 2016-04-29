#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='django-bleach',
    version="0.3.0",
    description='Easily use bleach with Django models and templates',
    author='Tim Heap',
    author_email='tim@timheap.me',
    url='https://bitbucket.org/tim_heap/django-bleach',
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
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
    ],
)
