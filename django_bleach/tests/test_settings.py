from django.core.exceptions import ImproperlyConfigured
from django.forms import Textarea
from django.test import TestCase
from mock import patch

from django_bleach.forms import get_default_widget
from django_bleach.utils import get_bleach_default_options

from testproject.constants import (
    ALLOWED_ATTRIBUTES, ALLOWED_PROTOCOLS,
    ALLOWED_STYLES, ALLOWED_TAGS
)
from testproject.forms import CustomBleachWidget


class TestBleachOptions(TestCase):

    @patch('django_bleach.utils.settings',
           BLEACH_ALLOWED_ATTRIBUTES=ALLOWED_ATTRIBUTES)
    def test_custom_attrs(self, settings):
        bleach_args = get_bleach_default_options()
        self.assertEqual(bleach_args['attributes'], ALLOWED_ATTRIBUTES)

    @patch('django_bleach.utils.settings',
           BLEACH_ALLOWED_PROTOCOLS=ALLOWED_PROTOCOLS)
    def test_custom_proto(self, settings):
        bleach_args = get_bleach_default_options()
        self.assertEqual(bleach_args['protocols'], ALLOWED_PROTOCOLS)

    @patch('django_bleach.utils.settings',
           BLEACH_ALLOWED_STYLES=ALLOWED_STYLES)
    def test_custom_styles(self, settings):
        bleach_args = get_bleach_default_options()
        self.assertEqual(bleach_args['styles'], ALLOWED_STYLES)

    @patch('django_bleach.utils.settings', BLEACH_ALLOWED_TAGS=ALLOWED_TAGS)
    def test_custom_tags(self, settings):
        bleach_args = get_bleach_default_options()
        self.assertEqual(bleach_args['tags'], ALLOWED_TAGS)

    @patch('django_bleach.utils.settings', BLEACH_STRIP_TAGS=True)
    def test_strip_tags(self, settings):
        bleach_args = get_bleach_default_options()
        self.assertEqual(bleach_args['strip'], True)

    @patch('django_bleach.utils.settings', BLEACH_STRIP_COMMENTS=True)
    def test_strip_comments(self, settings):
        bleach_args = get_bleach_default_options()
        self.assertEqual(bleach_args['strip_comments'], True)


class TestDefaultWidget(TestCase):
    """ Test form field widgets """

    def test_default_widget(self):
        self.assertEqual(get_default_widget(), Textarea)

    @patch('django_bleach.forms.settings',
           BLEACH_DEFAULT_WIDGET='testproject.forms.CustomBleachWidget')
    def test_custom_widget(self, settings):
        self.assertEqual(get_default_widget(), CustomBleachWidget)

    @patch('django_bleach.forms.settings',
           BLEACH_DEFAULT_WIDGET='testproject.forms.NoneExistentWidget')
    def test_attribute_err(self, settings):
        with self.assertRaises(ImproperlyConfigured):
            get_default_widget()

    @patch('django_bleach.forms.settings',
           BLEACH_DEFAULT_WIDGET='testproject.forms2.CustomBleachWidget')
    def test_import_Err(self, settings):
        with self.assertRaises(ImproperlyConfigured):
            get_default_widget()
