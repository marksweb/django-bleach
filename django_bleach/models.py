from django.db import models

from django_bleach import forms
from django_bleach.forms import default_widget
from django.conf import settings


class BleachField(models.TextField):

    def __init__(self, allowed_tags=None, allowed_styles=None,
        allowed_attributes=None, strip_tags=None, strip_comments=None,
        *args, **kwargs):

        super(BleachField, self).__init__(*args, **kwargs)

        self.formfield_defaults = {}

        if allowed_tags is not None:
            self.formfield_defaults['allowed_tags'] = allowed_tags
        if allowed_attributes is not None:
            self.formfield_defaults['allowed_attributes'] = allowed_attributes
        if allowed_styles is not None:
            self.formfield_defaults['allowed_styles'] = allowed_styles
        if strip_tags is not None:
            self.formfield_defaults['strip_tags'] = strip_tags
        if strip_comments is not None:
            self.formfield_defaults['strip_comments'] = strip_comments

    def formfield(self, **kwargs):
        options = {
            'form_class': forms.BleachField,
            'widget': default_widget,
        }
        options.update(self.formfield_defaults)
        options.update(kwargs)
        return super(BleachField, self).formfield(**options)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    # Bleach attributes don't influence on data representation so we use
    # default introspection rules of TextField
    add_introspection_rules([], ['^django_bleach\.models\.BleachField'])
