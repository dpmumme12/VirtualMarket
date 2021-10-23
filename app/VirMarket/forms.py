from django import forms
from django.contrib.auth.forms import UserCreationForm

### Forms used in the templates ###

class SignUpForm(UserCreationForm):
    """ Inherits Django;s UserCreationForm to create new users with no privileges """

    password1 = forms.CharField(label="Password", widget= forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget= forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
    username = forms.CharField(label='Usename', widget=forms.TextInput(attrs={
    'autocomplete': 'username', 
    'maxlength': '150', 
    'autocapitalize': 'none',
    'class': 'form-control'}))

class LoginForm(forms.Form):
    """ Form to get user's credentials to log them in """
    
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
    'autocomplete': 'username', 
    'maxlength': '150', 
    'autocapitalize': 'none',
    'class': 'form-control'}))

    password = forms.CharField(label="Password", widget= forms.PasswordInput(attrs={'autocomplete': 'password', 'class': 'form-control'}))