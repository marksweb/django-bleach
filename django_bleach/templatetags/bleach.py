import bleach

from django import template

register = template.Library()


bleach_args = {}

if "BLEACH_ALLOWED_TAGS" in settings:
    bleach_args["tags"] = settings.BLEACH_ALLOWED_TAGS

if "BLEACH_ALLOWED_ATTRIBUTES" in settings:
    bleach_args["attributes"] = settings.BLEACH_ALLOWED_ATTRIBUTES

if "BLEACH_ALLOWED_STYLES" in settings:
    bleach_args["styles"] = settings.BLEACH_ALLOWED_STYLES

if "BLEACH_STRIP_TAGS" in settings:
    bleach_args["strip"] = settings.BLEACH_STRIP_TAGS

if "BLEACH_STRIP_COMMENTS" in settings:
    bleach_args["strip_comments"] = settings.BLEACH_STRIP_COMMENTS


def bleach_value(value):
    return bleach.clean(value, **kwargs=bleach_args)
register.filter('bleach', bleach_value)
