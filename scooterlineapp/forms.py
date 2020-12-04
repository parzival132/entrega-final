from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuarios
from django import forms
class RegistrarForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
class SeleccionarScooter (forms.ModelForm):
    class Meta:
        model= Usuarios
        fields = ['username','last_name','email','modelo','zona']
        widgets = {
        'username':forms.TextInput(attrs={
            'readonly': 'readonly',
           
                }), 
                'last_name':forms.TextInput(attrs={
            'readonly': 'readonly',
           
                }), 
                'email':forms.TextInput(attrs={
            'readonly': 'readonly',
           
                }),}  


class ActualizaEstado (forms.ModelForm):
    class Meta:
        model= Usuarios
        fields = ['username','last_name','email','activo']
        widgets = {
        'username':forms.TextInput(attrs={
            'readonly': 'readonly',
           
                }), 
                'last_name':forms.TextInput(attrs={
            'readonly': 'readonly',
           
                }), 
                'email':forms.TextInput(attrs={
            'readonly': 'readonly',
           
            
                }),}               