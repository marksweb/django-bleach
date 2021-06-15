from django import forms
from django.test import TestCase, override_settings
from django_bleach import forms as bleach_forms
from .test_models import BleachContent


class BleachContentModelForm(forms.ModelForm):
    class Meta:
        model = BleachContent
        fields = '__all__'


class TestModelFormField(TestCase):
    @override_settings(BLEACH_DEFAULT_WIDGET='testproject.forms.CustomBleachWidget')
    def setUp(self):
        self.form_field = BleachContentModelForm().fields['content']
        self.model_field = BleachContent()._meta.get_field('content')
        self.default_widget_class = bleach_forms.get_default_widget()

    def test_formfield_type(self):
        """ Check content's form field is instance of BleachField
        """
        self.assertIsInstance(self.form_field, bleach_forms.BleachField)

    def test_custom_widget(self):
        """ Check content form field's widget is instance of default widget
        """
        self.assertIsInstance(self.form_field.widget, self.default_widget_class)

    def test_same_allowed_args(self):
        """ Check model and form's allowed arguments (tags, attributes, ...) are same
        """
        form_allowed_args: dict = self.form_field.bleach_options
        model_allowed_args: dict = self.model_field.bleach_kwargs

        for key in model_allowed_args.keys():
            self.assertEqual(model_allowed_args[key], form_allowed_args[key])
