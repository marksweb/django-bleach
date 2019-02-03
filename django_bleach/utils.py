from django.conf import settings


def get_bleach_default_options():
    bleach_args = {}
    bleach_settings = {
        'BLEACH_ALLOWED_TAGS': 'tags',
        'BLEACH_ALLOWED_ATTRIBUTES': 'attributes',
        'BLEACH_ALLOWED_STYLES': 'styles',
        'BLEACH_STRIP_TAGS': 'strip',
        'BLEACH_STRIP_COMMENTS': 'strip_comments',
        'BLEACH_ALLOWED_PROTOCOLS': 'protocols'
    }

    for setting, kwarg in bleach_settings.items():
        if hasattr(settings, setting):
            bleach_args[kwarg] = getattr(settings, setting)

    return bleach_args
