from django import forms

from django_bleach.forms import BleachField

#: List of allowed tags
ALLOWED_TAGS = [
    'a',
    'li',
    'ul',
]

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'li': ['class'],
    'ul': ['class']
}

ALLOWED_PROTOCOLS = [
    'http',
    'https',
    'data',
]


class BleachForm(forms.Form):
    """ Form for testing BleachField """
    no_tags = BleachField(
        max_length=100,
        strip_tags=True,
        allowed_tags=[]
    )

    bleach_strip = BleachField(
        max_length=100,
        strip_tags=True,
        allowed_tags=ALLOWED_TAGS
    )
    bleach_attrs = BleachField(
        max_length=100,
        strip_tags=False,
        allowed_tags=ALLOWED_TAGS,
        allowed_attributes=ALLOWED_ATTRIBUTES
    )
    bleach_attrs = BleachField(
        max_length=100,
        strip_tags=False,
        allowed_tags=ALLOWED_TAGS,
        allowed_attributes=ALLOWED_ATTRIBUTES,
        allowed_protocols=ALLOWED_PROTOCOLS
    )
