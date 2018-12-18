from django.conf import settings
from django.db import models

from bleach import clean

from .utils import get_bleach_default_options


class BleachField(models.TextField):
    def __init__(self, allowed_tags=None, allowed_attributes=None,
                 allowed_styles=None, strip_tags=None, strip_comments=None,
                 *args, **kwargs):

        super(BleachField, self).__init__(*args, **kwargs)

        self.bleach_kwargs = get_bleach_default_options()

        if allowed_tags:
            self.bleach_kwargs['tags'] = allowed_tags
        if allowed_attributes:
            self.bleach_kwargs['attributes'] = allowed_attributes
        if allowed_styles:
            self.bleach_kwargs['styles'] = allowed_styles
        if strip_tags:
            self.bleach_kwargs['strip'] = strip_tags
        if strip_comments:
            self.bleach_kwargs['strip_comments'] = strip_comments

    def pre_save(self, model_instance, add):
        clean_value = clean(
            getattr(model_instance, self.attname),
            **self.bleach_kwargs
        )
        setattr(model_instance, self.attname, clean_value)
        return clean_value


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    # Bleach attributes don't influence on data representation so we use
    # default introspection rules of TextField
    add_introspection_rules([], ['^django_bleach\.models\.BleachField'])
