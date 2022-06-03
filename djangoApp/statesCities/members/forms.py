from django import forms
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,required=True,help_text='Wpisz nazwe')
    email = forms.EmailField(max_length=254, help_text='Wprowadz maila')
    
    class Meta:
        model=UserAccount
        fields=[
            'name',
            'email',
            'password1',
            'password2',
        ]
    
    