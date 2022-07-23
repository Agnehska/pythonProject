from .models import *
from django.forms import ModelForm, TextInput, NumberInput, Select
from django import forms


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['name', 'age', 'master', 'status']

        widgets = {
            'name': TextInput(attrs={
                "class": 'form-control mb-3',
                "placeholder": 'Фамилия_Имя',
            }),
            'age': NumberInput(attrs={
                "class": 'form-control mb-3',
                "placeholder": 'Возраст',
            }),
            'master': TextInput(attrs={
                "class": 'form-control mb-3',
                "placeholder": 'Хозяин',
            }),
            'status': Select(attrs={
                "class": 'form-control mb-3',
            })
        }

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['status', 'earn']

        widgets = {
            'status': TextInput(attrs={
                "class": 'form-control mb-3',
                "placeholder": 'Добавить новый статус',
            }),
            'earn': NumberInput(attrs={
                "class": 'form-control mb-3',
                "placeholder": 'Доход',
            }),
        }

