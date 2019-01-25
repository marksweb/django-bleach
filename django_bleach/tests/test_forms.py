from django.test import TestCase

from testproject.forms import BleachForm


class TestBleachField(TestCase):

    def test_bleaching(self):
        """ Test values are bleached """
        test_data = {
            'no_tags': "<h1>Heading</h1>",
            'bleach_strip': """<script>alert("Hello World")</script>""",
            'bleach_attrs': "<a href=\"https://www.google.com\" "
                            "target=\"_blank\">google.com</a>"
        }
        form = BleachForm(data=test_data)
        form.is_valid()
        self.assertEqual(
            form.cleaned_data['no_tags'], 'Heading'
        )
        self.assertEqual(
            form.cleaned_data['bleach_strip'],
            'alert("Hello World")'
        )
        self.assertEqual(
            form.cleaned_data['bleach_attrs'],
            '<a href="https://www.google.com">google.com</a>'
        )

    def test_tags(self):
        """ Test allowed tags are rendered"""
        test_data = {
            'no_tags': "No tags here",
            'bleach_strip': "<ul><li>one</li><li>two</li></ul>",
            'bleach_attrs': "<a href=\"https://www.google.com\" "
                            "title=\"Google\">google.com</a>"
        }
        form = BleachForm(data=test_data)
        form.is_valid()
        self.assertEqual(form.cleaned_data['no_tags'], 'No tags here')

        self.assertEqual(
            form.cleaned_data['bleach_strip'],
            test_data['bleach_strip']
        )
        self.assertEqual(
            form.cleaned_data['bleach_attrs'],
            test_data['bleach_attrs']
        )

    def test_attrs(self):
        """ Test allowed attributes are rendered """
        list_html = "<ul class=\"our-list\">" \
                    "<li class=\"list-item\">one</li>" \
                    "<li>two</li>" \
                    "</ul>"
        test_data = {
            'no_tags': list_html,
            'bleach_strip': list_html,
            'bleach_attrs': list_html,
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
