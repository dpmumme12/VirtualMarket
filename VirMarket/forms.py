from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget= forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'test'}))
    password2 = forms.CharField(label="Password", widget= forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'test'}))
    username = forms.CharField(label='Usename', widget=forms.TextInput(attrs={
    'autocomplete': 'username', 
    'maxlength': '150', 
    'autocapitalize': 'none',
    'class': 'test'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
    'autocomplete': 'username', 
    'maxlength': '150', 
    'autocapitalize': 'none',
    'class': 'test'}))

    password = forms.CharField(label="Password", widget= forms.PasswordInput(attrs={'autocomplete': 'password', 'class': 'test'}))