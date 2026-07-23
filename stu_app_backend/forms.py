from django import forms
from django.contrib.auth.models import User
from .models import Student



class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )


    phone = forms.CharField(
        max_length=15
    )


    branch = forms.CharField(
        max_length=50
    )


    year = forms.CharField(
        max_length=20
    )



    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password'
        ]