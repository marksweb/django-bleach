from django.db import models

from bleach.css_sanitizer import CSSSanitizer

from django_bleach.models import BleachField


class Person(models.Model):
    name = models.CharField(max_length=20)
    biography = BleachField(
        max_length=100,
        verbose_name='Person biography',
        allowed_tags=['p', 'a', 'li', 'ul', 'strong'],
        allowed_attributes=['class', 'href', 'style'],
        allowed_protocols=['http', 'https'],
        css_sanitizer=CSSSanitizer(allowed_css_properties=['color', 'background-color'])
    )
