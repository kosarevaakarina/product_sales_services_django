from django import forms

from catalog.models import *

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                   'радар']


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if cleaned_data.lower() in FORBIDDEN_WORDS:
            raise forms.ValidationError(f"Нельзя вносить слово {cleaned_data}, замените его на другое")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in FORBIDDEN_WORDS:
            raise forms.ValidationError(f"Нельзя вносить слово {cleaned_data}, замените его на другое")
        return cleaned_data


class VersionForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'num_of_version', 'title',)
