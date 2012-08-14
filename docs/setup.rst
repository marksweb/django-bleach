=====
Setup
=====

.. _setup:

1.  Get the source from the `Git repository`_ or install it from the Python
    Package Index by running ``pip install django-bleach``.

2.  Add ``django_bleach`` to the ``INSTALLED_APPS`` setting::

        INSTALLED_APPS += (
            'django_bleach',
        )

3. Configure ``django_bleach``. It comes with some sensible defaults, but you
   will probably want to tweak the settings for your application. See the
   :role:`settings` page for more information

3. Add a ``django_bleach.models.BleachField`` to a model, a
   ``django_bleach.forms.BleachField`` to a form, or use the ``bleach``
   template filter in your templates.

.. _Git repository: http://bitbucket.org/ionata/django-bleach/
