from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Musician


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    birth = forms.DateField(widget=DateInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth', 'email', 'password1', 'password2', )


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class MusicianUpdateForm(forms.ModelForm):
    class Meta:
        model = Musician
        birthday = forms.DateField(widget=DateInput)
        fields = ['birthday', 'city', 'instrument', 'playing_level', 'image']


class SearchForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['instrument', 'playing_level']
