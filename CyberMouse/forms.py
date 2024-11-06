""""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="envoie un bon mail")

    class Meta:
        model = User
        field = ('username', 'email', 'password1' 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_date.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Mail deja utilisé.")
        return email

    def clean_username(self):
        username = self.cleaned_date.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Deja pris")
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Deja utilise")
        return phone_number
"""