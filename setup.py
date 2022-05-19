#!/usr/bin/env python
import codecs
import os
import re
import sys
from setuptools import find_packages, setup
from setuptools.command.test import test as test_command


try:
    from sphinx.setup_command import BuildDoc
except ImportError:
    BuildDoc = None


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
        import shlex
        import tox
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
        fr"^{variable} = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


name = 'django-bleach'
release = find_variable('__version__', 'django_bleach', '__init__.py')
version = release.rstrip('.')

setup(
    name=name,
    version=version,
    description='Easily use bleach with Django models and templates',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    author='Tim Heap',
    maintainer='Mark Walker',
    maintainer_email='theshow+django-bleach@gmail.com',
    url='https://github.com/marksweb/django-bleach',
    license='MIT',
    packages=find_packages(exclude=('testproject*',)),
    install_requires=[
        'bleach[css]>=5,<6',
        'Django>=1.11',
    ],
    python_requires='>=3.8',
    tests_require=[
        'bleach[css]>=5,<6',
        'mock',
        'sphinx',
        'tox'
    ],
    cmdclass={
        'build_sphinx': BuildDoc,
        'test': Tox
    },
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs'),
            'build_dir': ('setup.py', './docs/_build')
        }
    },
    package_data={},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Development Status :: 5 - Production/Stable',
    ],
    project_urls={
        'Documentation': 'https://django-bleach.readthedocs.io/',
        'Release notes': 'https://github.com/marksweb/django-bleach/blob/main/CHANGELOG.md',
        'Issues': 'https://github.com/marksweb/django-bleach/issues',
        'Source': 'https://github.com/marksweb/django-bleach',
    }
)
