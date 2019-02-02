django-bleach - Bleach and sanitise user HTML
=============================================

.. image:: https://travis-ci.org/marksweb/django-bleach.svg?branch=master
   :target: https://travis-ci.org/marksweb/django-bleach

.. image:: http://img.shields.io/pypi/v/django-bleach.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-bleach/
    :alt: Latest Version

.. image:: https://codecov.io/gh/marksweb/django-bleach/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/marksweb/django-bleach

.. image:: https://api.codacy.com/project/badge/Grade/c34f923ab0a84a6f96728866c749d511
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/marksweb/django-bleach?utm_source=github.com&utm_medium=referral&utm_content=marksweb/django-bleach&utm_campaign=Badge_Grade_Dashboard

.. image:: http://img.shields.io/pypi/dm/django-bleach.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-bleach/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/django-bleach.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-bleach/
    :alt: License

Bleach_ is a Python module that takes any HTML input, and returns
valid, sanitised HTML that contains only an allowed subset of HTML tags,
attributes and styles. ``django-bleach`` is a Django app that makes using
``bleach`` extremely easy.

Setup
-----

1. Install ``django-bleach`` via ``pip``::

    pip install django-bleach

2. Add ``django-bleach`` to your ``INSTALLED_APPS``::

        INSTALLED_APPS = [
            # ...
            'django_bleach',
            # ...
        ]

3. Select some sensible defaults for the allowed tags, attributes and styles;
   and the behaviour when unknown tags are encountered. Each of these are
   optional, and default to using the ``bleach`` defaults. See the
   `bleach documentation`_::

        # Which HTML tags are allowed
        BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 'a']

        # Which HTML attributes are allowed
        BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style']

        # Which CSS properties are allowed in 'style' attributes (assuming
        # style is an allowed attribute)
        BLEACH_ALLOWED_STYLES = [
            'font-family', 'font-weight', 'text-decoration', 'font-variant']

        # Strip unknown tags if True, replace with HTML escaped characters if
        # False
        BLEACH_STRIP_TAGS = True

        # Strip comments, or leave them in.
        BLEACH_STRIP_COMMENTS = False

4. Select the default widget for bleach fields. This defaults to
   ``django.forms.Textarea``, but you will probably want to replace it with a
   WYSIWYG editor, or something similar::

        # Use the CKEditorWidget for bleached HTML fields
           BLEACH_DEFAULT_WIDGET = 'wysiwyg.widgets.WysiwygWidget'

   I use `django-ckeditor`_ in my projects, but what you use is up to you.

Usage
-----

In your models
**************

``django-bleach`` provides three ways of creating bleached output. The simplest
way of including user-editable HTML content that is automatically sanitised is
by using the ``BleachField`` model field::

    # in app/models.py

    from django import models
    from django_bleach.models import BleachField

    class Post(models.Model):

        title = models.CharField()
        content = BleachField()

        # ...

``BleachField`` takes the following arguments, to customise the output of
``bleach``. See the `bleach documentation`_ for their use:

* ``allowed_tags``
* ``allowed_attributes``
* ``allowed_styles``
* ``strip_tags``
* ``strip_comments``

In addition to the ``bleach``-specific arguments, the ``BleachField`` model field
accepts all of the normal field attributes. Behind the scenes, it is a
``TextField``, and accepts all the same arguments as the default ``TextField`` does.

The ``BleachField`` model field makes use of the ``BleachField`` form field to do
all of the work. It provides no sanitisation facilities itself. This is
considered a bug, but a clean solution has not yet been implemented. Any pull
requests fixing this will be gratefully applied. As long as the ``BleachField``
model field is only used with ``BleachField`` form fields, there will be no
problem. If this is not the case, sanitised HTML can not be guaranteed.

In your forms
*************

A ``BleachField`` form field is provided. This field sanitises HTML input from
the user, and presents safe, clean HTML to your Django application. This is
where most of the work is done.

In your templates
*****************

If you have a piece of content from somewhere that needs to be printed in a
template, you can use the ``bleach`` filter::

    {% load bleach_tags %}

    {{ some_unsafe_content|bleach }}

If filter has no arguments it uses default settings defined in your
application settings. You can override allowed tags by specifying them
as a parameter to the filter::

    {{ some_unsafe_content|bleach:"p,span" }}

There is also ``bleach_linkify`` which uses the linkify_ function of bleach
which converts URL-like strings in an HTML fragment to links

This function converts strings that look like URLs, domain names and email
addresses in text that may be an HTML fragment to links, while preserving:

1. links already in the string
2. urls found in attributes
3. email addresses


.. _bleach: https://github.com/jsocol/bleach "Bleach"
.. _bleach documentation: https://github.com/jsocol/bleach/blob/master/README.rst "Bleach documentation - parameters"
.. _django-ckeditor: https://github.com/shaunsephton/django-ckeditor "Django CKEditor widget"
.. _linkify: https://bleach.readthedocs.io/en/latest/linkify.html?highlight=linkify#bleach.linkify "linkify"
