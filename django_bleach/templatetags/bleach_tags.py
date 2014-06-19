import bleach

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


bleach_args = {}

possible_settings = {
    'BLEACH_ALLOWED_TAGS': 'tags',
    'BLEACH_ALLOWED_ATTRIBUTES': 'attributes',
    'BLEACH_ALLOWED_STYLES': 'styles',
    'BLEACH_STRIP_TAGS': 'strip',
    'BLEACH_STRIP_COMMENTS': 'strip_comments',
}

for setting, kwarg in possible_settings.items():
    if hasattr(settings, setting):
        bleach_args[kwarg] = getattr(settings, setting)


def bleach_value(value):
    bleached_value = bleach.clean(value, **bleach_args)
    return mark_safe(bleached_value)

register.filter('bleach', bleach_value)

@register.filter
def bleach_linkify(value):
    return bleach.linkify(value, parse_email=True)