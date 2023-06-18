from django import forms

from catalog.models import *

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                   'радар']


class FormStyleMixin:
    """Класс-миксин для стилизации форм"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):
    """Форма для создания товара"""
    class Meta:
        model = Product
        exclude = ('user', 'is_published')

    def clean_name(self):
        """Валидация названия товара (запрещает вводить слова из списка)"""
        cleaned_data = self.cleaned_data['name']
        if cleaned_data.lower() in FORBIDDEN_WORDS:
            raise forms.ValidationError(f"Нельзя вносить слово {cleaned_data}, замените его на другое")
        return cleaned_data

    def clean_description(self):
        """Валидация описания товара (запрещает вводить слова из списка)"""
        cleaned_data = self.cleaned_data['description']
        if cleaned_data.lower() in FORBIDDEN_WORDS:
            raise forms.ValidationError(f"Нельзя вносить слово {cleaned_data}, замените его на другое")
        return cleaned_data


class ProductFormCutted(ProductForm, FormStyleMixin, forms.ModelForm):
    """Форма для изменения полей описания и категории"""
    class Meta:
        model = Product
        fields = ('description', 'category')


class VersionForm(FormStyleMixin, forms.ModelForm):
    """Форма, описывающая версию"""
    class Meta:
        model = Version
        fields = ('product', 'num_of_version', 'title',)
