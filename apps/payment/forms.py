from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    cities = forms.CharField(label='City', widget=forms.TextInput(attrs={
                'class': 'orders__input',
                'id': 'cities'
            }))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'post_code', 'country', 'cities', 'address']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'orders__input',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'orders__input',
            }),
            'address': forms.TextInput(attrs={
                'class': 'orders__input',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'orders__input'
            }),
            'post_code': forms.NumberInput(attrs={
                'class': 'orders__input'
            }),
            'country': forms.Select(attrs={
                'class': 'orders__input',

            })
        }
