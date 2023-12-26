from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Service


class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', max_length=30, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=30, required=True)
    username = forms.CharField(label='Логин', max_length=150, )
    avatar = forms.ImageField(label='Фото профиля', required=False)
    age = forms.IntegerField(label='Возраст')

    class Meta:
        model = CustomUser
        fields = ('avatar', 'first_name', 'last_name', 'age', 'username', 'password1', 'password2')


class ServiceForm(forms.ModelForm):
    name = forms.CharField(label='Название товара', max_length=40, required=True)
    description = forms.CharField(label='Описание', max_length=60, required=True)
    price = forms.CharField(label='Цена', required=True)
    photo = forms.ImageField(label='Фото товара', required=True)

    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'photo']
