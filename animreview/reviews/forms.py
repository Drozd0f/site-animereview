from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['universe'].empty_label = "Вселенная не выбрана"
        self.fields['title'].label = "Название"
        self.fields['text'].label = "Описание"
        self.fields['photo'].label = "Фото"
        self.fields['rating'].label = "Рейтинг"
        self.fields['universe'].label = "Вселенная"
        self.fields['genre'].label = "Жанр"

    class Meta:
        model = Posts
        exclude = ('user', 'slug',)
        fields = ['title', 'text', 'photo', 'rating', 'universe', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'add-post-text'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'add-post-description'}),
            'photo': forms.FileInput(attrs={'class': 'add-post-photo'}),
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 10, 'class': 'add-post-rating'}),
            'universe': forms.Select(attrs={'class': 'add-post-universe'}),
            'genre': forms.CheckboxSelectMultiple(attrs={'class': 'add-post-genre'})
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


# class UserUpdateProfile(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"
