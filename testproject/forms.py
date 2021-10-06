from django import forms

from django_bleach.forms import BleachField
from testproject.constants import ALLOWED_ATTRIBUTES, ALLOWED_PROTOCOLS, ALLOWED_STYLES, ALLOWED_TAGS
from testproject.models import Person


class CustomBleachWidget(forms.Textarea):

    def __init__(self, attrs=None):
        default_attrs = {'rows': 15, 'cols': 60}
        default_attrs.update(attrs or {})
        super().__init__(attrs=default_attrs)


class BleachForm(forms.Form):
    """ Form for testing BleachField """
    no_tags = BleachField(
        max_length=100,
        strip_tags=True,
        allowed_tags=[]
    )

    no_strip = BleachField(
        max_length=100,
        allowed_tags=None,
        allowed_attributes=None
    )

    bleach_strip = BleachField(
        max_length=100,
        strip_comments=True,
        strip_tags=True,
        allowed_tags=ALLOWED_TAGS
    )
    bleach_attrs = BleachField(
        max_length=100,
        strip_tags=False,
        allowed_tags=ALLOWED_TAGS,
        allowed_protocols=ALLOWED_PROTOCOLS,
        allowed_attributes=ALLOWED_ATTRIBUTES
    )
    bleach_styles = BleachField(
        max_length=100,
        strip_tags=False,
        allowed_attributes=['style'],
        allowed_tags=ALLOWED_TAGS,
        allowed_styles=ALLOWED_STYLES
    )


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
