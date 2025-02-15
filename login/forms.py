from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='Usuario', min_length=5, max_length=150, widget=forms.TextInput(attrs={'placeholder': 'El usuario debe tener al menos 4 caracteres'}))  
    email = forms.EmailField(label='E-Mail')  
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'La contraseña debe tener al menos 8 caracteres'}))  
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)  
  
    def clean_username(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El Usuario ingresado ya existe")  
        return username  
  
    def clean_email(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("El E-Mail ingresado ya existe")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las Contraseñas no coinciden")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user  