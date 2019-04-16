from django.db import models
from django.test import TestCase

from django_bleach.models import BleachField
from testproject.constants import (
    ALLOWED_ATTRIBUTES, ALLOWED_PROTOCOLS,
    ALLOWED_STYLES, ALLOWED_TAGS
)


class BleachContent(models.Model):
    """ Bleach test model"""
    content = BleachField(
        allowed_attributes=ALLOWED_ATTRIBUTES,
        allowed_protocols=ALLOWED_PROTOCOLS,
        allowed_styles=ALLOWED_STYLES,
        allowed_tags=ALLOWED_TAGS,
        strip_comments=True,
        strip_tags=True
    )


class TestBleachModelField(TestCase):
    """ Test model field """

    def test_bleaching(self):
        """ Test values are bleached """
        test_data = {
            'no_tags': "<h1>Heading</h1>",
            'no_strip': "<h1>Heading</h1>",
            'bleach_strip': """<script>alert("Hello World")</script>""",
            'bleach_attrs': "<a href=\"http://www.google.com\" "
                            "target=\"_blank\">google.com</a>",
            'bleach_styles': "<li style=\"color: white\">item</li>",
            'bleach_comment': "<!-- this is a comment -->",
        }
        expected_values = {
            'no_tags': "Heading",
            'no_strip': "Heading",
            'bleach_strip': """alert("Hello World")""",
            'bleach_attrs':
                "<a>google.com</a>",
            'bleach_styles': "<li style=\"color: white;\">item</li>",
            'bleach_comment': ""
        }

        for key, value in test_data.items():
            obj = BleachContent.objects.create(content=value)
            self.assertEqual(obj.content, expected_values[key])


class BleachNullableContent(models.Model):
    """ Bleach test model"""
    content = BleachField(
        allowed_attributes=ALLOWED_ATTRIBUTES,
        allowed_protocols=ALLOWED_PROTOCOLS,
        allowed_styles=ALLOWED_STYLES,
        allowed_tags=ALLOWED_TAGS,
        strip_comments=True,
        strip_tags=True,
        blank=True,
        null=True
    )


class TestBleachNullableModelField(TestCase):
    """ Test model field """

    def test_bleaching(self):
        """ Test values are bleached """
        test_data = {
            'none': None,
            'empty': "",
            'whitespaces': "   ",
            'linebreak': "\n",
        }
        expected_values = {
            'none': None,
            'empty': "",
            'whitespaces': "   ",
            'linebreak': "\n",
        }

        for key, value in test_data.items():
            obj = BleachNullableContent.objects.create(content=value)
            self.assertEqual(obj.content, expected_values[key])
