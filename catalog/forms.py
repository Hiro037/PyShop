from django import forms
from catalog.models import Products

class ProductForm(forms.ModelForm):
    # Эта форма используется для добавления товаров на сайте
    class Meta:
        model = Products
        fields = ['name', 'description', 'image', 'category', 'price']


class ContactsForm(forms.Form):
    # Форма для контактов
    fields = ['name', 'number', 'message']