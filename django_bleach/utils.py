from django.conf import settings


def get_bleach_default_options():
    bleach_args = {}

    if hasattr(settings, "BLEACH_ALLOWED_TAGS"):
        bleach_args["tags"] = settings.BLEACH_ALLOWED_TAGS

    if hasattr(settings, "BLEACH_ALLOWED_ATTRIBUTES"):
        bleach_args["attributes"] = settings.BLEACH_ALLOWED_ATTRIBUTES

    if hasattr(settings, "BLEACH_ALLOWED_STYLES"):
        bleach_args["styles"] = settings.BLEACH_ALLOWED_STYLES

    if hasattr(settings, "BLEACH_STRIP_TAGS"):
        bleach_args["strip"] = settings.BLEACH_STRIP_TAGS

    if hasattr(settings, "BLEACH_STRIP_COMMENTS"):
        bleach_args["strip_comments"] = settings.BLEACH_STRIP_COMMENTS

    return bleach_args
