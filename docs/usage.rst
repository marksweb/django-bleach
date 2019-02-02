.. _usage:

=====
Usage
=====

.. _models:

In your models
==============

``django-bleach`` provides three ways of creating bleached output. The simplest
way of including user-editable HTML content that is automatically sanitised is
by using the BleachField model field::

    # in app/models.py

    from django import models
    from django_bleach.models import BleachField

    class Post(models.Model):

        title = models.CharField()
        content = BleachField()

``BleachField`` takes the following arguments, to customise the output of
``bleach``.

See the bleach documentation for their use:

* ``allowed_tags``
* ``allowed_attributes``
* ``allowed_styles``
* ``allowed_protocols``
* ``strip_tags``
* ``strip_comments``

In addition to the bleach-specific arguments, the ``BleachField`` model field
accepts all of the normal field attributes. Behind the scenes, it is a
``TextField``, and accepts all the same arguments as ``TextField``.

The field does not specify any formfield to use, and falls back on the default
``CharField`` and ``Textarea`` used by ``TextFields``. You must override the
form field or widget yourself if you need something different.

.. _forms:

In your forms
=============

A ``BleachField`` form field is provided. This field sanitises HTML input from
the user, and presents safe, clean HTML to your Django application. This is
where most of the work is done. Usually you will want to use a ``BleachField``
model field, as opposed to the form field, but if you want, you can just use
the form field. One possible use case for this set up is to force user input to
be bleached, but allow administrators to add any content they like via another
form (e.g. the admin site)::

    # in app/forms.py

    from django import forms
    from django_bleach.forms import BleachField

    from app.models import Post

    class PostForm(forms.ModelForm):
        class Meta:
            model = Post

            fields = ['title', 'content']

        content = BleachField()

The ``BleachField`` form field takes exactly the same arguments as the
``BleachField`` model field above.

.. _templates:

In your templates
=================

If you have a piece of content from somewhere that needs to be printed in a
template, you can use the ``bleach`` filter::

    {% load bleach_tags %}

    {{ some_unsafe_content|bleach }}

It uses the ``ALLOWED_TAGS`` setting in your application, or optionally,
``bleach`` can pass tags::

    {% load bleach_tags %}

    {{ some_unsafe_content|bleach:"p,span" }}

If you have content which doesn't contain HTML, but contains links or email
addresses, you can also use the ``bleach_linkify`` filter to convert
content to links::


    {% load bleach_tags %}

    {{ some_safe_content|bleach_linkify }}

