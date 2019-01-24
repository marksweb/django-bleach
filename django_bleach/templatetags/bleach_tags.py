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


@register.filter(name='bleach')
def bleach_value(value, tags=None):
    if tags is not None:
        args = bleach_args.copy()
        args['tags'] = tags.split(',')
    else:
        args = bleach_args
    bleached_value = bleach.clean(value, **args)
    return mark_safe(bleached_value)


@register.filter
def bleach_linkify(value):
    """
    Convert URL-like strings in an HTML fragment to links

    This function converts strings that look like URLs, domain names and email
    addresses in text that may be an HTML fragment to links, while preserving:

        1. links already in the string
        2. urls found in attributes
        3. email addresses
    """
    return bleach.linkify(value, parse_email=True)
