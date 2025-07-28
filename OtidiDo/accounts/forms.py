from django import forms
from django.contrib.auth.forms import UserCreationForm

from OtidiDo.accounts.models import AppUser, Traveler


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password1', 'password2')

        labels = {
            'username': 'Потребителско име',
            'email': 'email',
            'password1': 'Парола',
            'password2': 'Повтори паролата',
        }
        help_texts = {
            'password2': 'Повтори паролата'
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['avatar', 'bio']

        labels = {
            'avatar': 'Снимка',
            'bio': 'Повече за мен',
        }

