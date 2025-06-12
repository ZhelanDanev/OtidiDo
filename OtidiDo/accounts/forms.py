from django import forms
from django.contrib.auth.forms import UserCreationForm

from OtidiDo.accounts.models import AppUser, Traveler


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['avatar', 'bio']
