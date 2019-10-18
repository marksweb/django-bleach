#!/usr/bin/env python
import codecs
import os
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as test_command


class Tox(test_command):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)


def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_variable(variable, *parts):
    version_file = read(*parts)
    version_match = re.search(
        r"^{0} = ['\"]([^'\"]*)['\"]".format(variable), version_file, re.M
    )
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


version = find_variable('__version__', 'django_bleach', '__init__.py')

if sys.argv[-1] == 'build':
    os.system('python setup.py sdist bdist_wheel')
    sys.exit()


if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()


setup(
    name='django-bleach',
    version=version,
    description='Easily use bleach with Django models and templates',
    long_description=read('README.rst'),
    author=find_variable('__author__', 'django_bleach', '__init__.py'),
    author_email='theshow@gmail.com',
    url='https://github.com/marksweb/django-bleach',
    license='MIT',
    packages=find_packages(exclude=('testproject*',)),
    install_requires=[
        'bleach>=1.5.0',
        'Django>=1.11',
    ],
    tests_require=[
        'bleach>=1.5.0',
        'mock',
        'tox'
    ],
    cmdclass={'test': Tox},
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
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
    ],
)
