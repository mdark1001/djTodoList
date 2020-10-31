"""
@author mdark1001 | Miguel Cabrera R. <miguel.cabrera.app@gmail.com>
@date 26/10/20
@project 
@name forms
"""
from django import forms
from django.contrib.auth.models import User

from .models import Profile


class SignupForm(forms.Form):
    """ Singout form class"""

    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nombre de usuario'}
        ),
        label='Nombre de usuario'
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Contraseña'}),
        label='Contraseña'
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Confirmar Contraseña'}
        ),
        label='Confirmar contraseña'
    )
    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Nombre(s)'}
        ),
        label='Nombre(s)'
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Apellido(s)'}
        ),
        label='Apellido(s)'
    )
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline', 'placeholder': 'Email'}
        ),
        required=True,
        label='Correo electrónico'
    )

    def clean_username(self):
        """ Validate username unique"""
        username = self.cleaned_data.get('username')
        result = User.objects.filter(username=username).exists()
        if result:
            raise forms.ValidationError('El Nombre de usuario ya se encuentra en uso, por favor intenteló con otro ')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas deben ser iguales')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
