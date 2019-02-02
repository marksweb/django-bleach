.. _settings:

========
Settings
========

Configuring ``bleach``
======================

You can configure how ``bleach`` acts for your whole project using the
following settings. These settings map directly to the ``bleach`` parameters of
the same name, so see the ``bleach`` `documentation` for more information. Each
of these have a sensible default set by ``bleach``, and each of these are
completely optional::

    # Which HTML tags are allowed
    BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 'a']

    # Which HTML attributes are allowed
    BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style']

    # Which CSS properties are allowed in 'style' attributes (assuming style is
    # an allowed attribute)
    BLEACH_ALLOWED_STYLES = [
        'font-family', 'font-weight', 'text-decoration', 'font-variant'
    ]

    # Which protocols (and pseudo-protocols) are allowed in 'src' attributes
    # (assuming src is an allowed attribute)
    BLEACH_ALLOWED_PROTOCOLS = [
        'http', 'https', 'data'
    ]

    # Strip unknown tags if True, replace with HTML escaped characters if False
    BLEACH_STRIP_TAGS = True

    # Strip HTML comments, or leave them in.
    BLEACH_STRIP_COMMENTS = False

You can override each of these for individual ``BleachField`` form and model
fields if you need to. Simply pass in one of the following settings you want to
override as a named parameter to the ``BleachField``::

* ``allowed_tags``
* ``allowed_attributes``
* ``allowed_styles``
* ``allowed_protocols``
* ``strip_tags``
* ``strip_comments``

An example, where blog posts should be allowed to contain images and headings::

    # in app/models.py

    from django import models
    from django_bleach.models import BleachField

    class Post(models.Model):

        title = models.CharField()
        content = BleachField(allowed_tags=[
            'p', 'b', 'i', 'u', 'em', 'strong', 'a',
            'img', 'h3', 'h4', 'h5', 'h6'])

Default form widget
===================

By default, a ``BleachField`` will use a ``django.forms.Textarea`` widget. This
is obviously not great for users. You can override this to use a custom widget
in your project. You will probably want to use a WYSIWYG editor, or something
similar::

    BLEACH_DEFAULT_WIDGET = 'wysiwyg.widgets.WysiwygWidget'

I use ``django-ckeditor`` in my projects, but what you use is up to you.


.. _documentation: http://bleach.readthedocs.org/en/latest/index.html
