from django.db import models

from django_bleach import forms
from django_bleach.utils import get_bleach_default_options
from django_bleach.forms import default_widget


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

    def south_field_triple(self):
        return ('django_bleach.models.BleachField', [],
            self.formfield_defaults)
