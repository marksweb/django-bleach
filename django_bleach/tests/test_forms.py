# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils.safestring import SafeString
from mock import patch

from django_bleach.forms import BleachField
from testproject.forms import BleachForm


class TestBleachField(TestCase):

    def test_empty(self):
        """ Test that the empty_value arg is returned for any input empty value """
        for requested_empty_value in ('', None):
            field = BleachField(empty_value=requested_empty_value)
            for empty_value in field.empty_values:
                self.assertEqual(field.to_python(empty_value), requested_empty_value)

    def test_return_type(self):
        """ Test bleached values are SafeString objects """
        field = BleachField()
        self.assertIsInstance(field.to_python("some text"), SafeString)

    def test_bleaching(self):
        """ Test values are bleached """
        test_data = {
            'no_tags': "<h1>Heading</h1>",
            'no_strip': "<h1>Heading</h1>",
            'bleach_strip': "<!-- script here -->"
                            "<script>alert(\"Hello World\")</script>",
            'bleach_attrs': "<a href=\"https://www.google.com\" "
                            "target=\"_blank\">google.com</a>",
            'bleach_styles': "<li style=\"color: white\">item</li>"
        }
        form = BleachForm(data=test_data)
        form.is_valid()
        self.assertEqual(
            form.cleaned_data['no_tags'], 'Heading'
        )
        self.assertEqual(
            form.cleaned_data['no_strip'],
            '&lt;h1&gt;Heading&lt;/h1&gt;'
        )
        self.assertEqual(
            form.cleaned_data['bleach_strip'],
            'alert("Hello World")'
        )
        self.assertEqual(
            form.cleaned_data['bleach_attrs'],
            '<a href="https://www.google.com">google.com</a>'
        )
        self.assertNotEqual(
            form.cleaned_data['bleach_styles'],
            test_data['bleach_styles']
        )

    def test_tags(self):
        """ Test allowed tags are rendered"""
        test_data = {
            'no_tags': "<p>No tags here</p>",
            'no_strip': "No tags here",
            'bleach_strip': "<ul><li>one</li><li>two</li></ul>",
            'bleach_attrs': "<a href=\"https://www.google.com\" "
                            "title=\"Google\">google.com</a>",
            'bleach_styles': "<li style=\"color: white;\">item</li>"
        }
        form = BleachForm(data=test_data)
        form.is_valid()
        self.assertEqual(form.cleaned_data['no_tags'], "No tags here")
        self.assertEqual(form.cleaned_data['no_strip'], "No tags here")

        self.assertEqual(
            form.cleaned_data['bleach_strip'],
            test_data['bleach_strip']
        )
        self.assertEqual(
            form.cleaned_data['bleach_attrs'],
            test_data['bleach_attrs']
        )
        self.assertEqual(
            form.cleaned_data['bleach_styles'],
            test_data['bleach_styles']
        )

    def test_attrs(self):
        """ Test allowed attributes are rendered """
        list_html = "<ul class=\"our-list\">" \
                    "<li class=\"list-item\">one</li>" \
                    "<li>two</li>" \
                    "</ul>"
        test_data = {
            'no_strip': "",
            'no_tags': list_html,
            'bleach_strip': list_html,
            'bleach_attrs': list_html,
            'bleach_styles': list_html
        }
        form = BleachForm(data=test_data)
        form.is_valid()
        self.assertEqual(form.cleaned_data['no_tags'], 'onetwo')

        self.assertEqual(
            form.cleaned_data['bleach_strip'],
            '<ul><li>one</li><li>two</li></ul>'
        )
        self.assertEqual(
            form.cleaned_data['bleach_attrs'],
            test_data['bleach_strip']
        )
        self.assertEqual(
            form.cleaned_data['bleach_styles'],
            '<ul><li>one</li><li>two</li></ul>'
        )

    @patch('django_bleach.forms.settings',
           BLEACH_DEFAULT_WIDGET='testproject.forms.CustomBleachWidget')
    def test_custom_widget(self, settings):

        self.assertEqual(
            settings.BLEACH_DEFAULT_WIDGET,
            'testproject.forms.CustomBleachWidget'
        )
        test_data = {
            'no_tags': "<h1>Heading</h1>",
            'no_strip': "<h1>Heading</h1>",
            'bleach_strip': "<!-- script here -->"
                            "<script>alert(\"Hello World\")</script>",
            'bleach_attrs': "<a href=\"http://www.google.com\" "
                            "target=\"_blank\">google.com</a>",
            'bleach_styles': "<li style=\"color: white\">item</li>"
        }
        form = BleachForm(data=test_data)
        form.is_valid()
        self.assertEqual(
            form.cleaned_data['no_tags'], 'Heading'
        )
        self.assertEqual(
            form.cleaned_data['no_strip'],
            '&lt;h1&gt;Heading&lt;/h1&gt;'
        )
        self.assertEqual(
            form.cleaned_data['bleach_strip'],
            'alert("Hello World")'
        )
        self.assertEqual(
            form.cleaned_data['bleach_attrs'],
            '<a>google.com</a>'
        )
        self.assertNotEqual(
            form.cleaned_data['bleach_styles'],
            test_data['bleach_styles']
        )

    @patch('django_bleach.forms.settings', BLEACH_DEFAULT_WIDGET='testproject.forms.CustomBleachWidget')
    def test_custom_widget2(self, settings):
        self.assertEqual(
            settings.BLEACH_DEFAULT_WIDGET,
            'testproject.forms.CustomBleachWidget'
        )
        test_data = {
            'no_tags': "<h1>Heading</h1>",
            'no_strip': "<h1>Heading</h1>",
            'bleach_strip': "<!-- script here -->"
                            "<script>alert(\"Hello World\")</script>",
            'bleach_attrs': "<a href=\"https://www.google.com\" "
                            "target=\"_blank\">google.com</a>",
            'bleach_styles': "<li style=\"color: white\">item</li>"
        }
        form = BleachForm(data=test_data)
        form.is_valid()
        self.assertEqual(
            form.cleaned_data['no_tags'], 'Heading'
        )
        self.assertEqual(
            form.cleaned_data['no_strip'],
            '&lt;h1&gt;Heading&lt;/h1&gt;'
        )
        self.assertEqual(
            form.cleaned_data['bleach_strip'],
            'alert("Hello World")'
        )
        self.assertEqual(
            form.cleaned_data['bleach_attrs'],
            '<a href="https://www.google.com">google.com</a>'
        )
        self.assertNotEqual(
            form.cleaned_data['bleach_styles'],
            test_data['bleach_styles']
        )
