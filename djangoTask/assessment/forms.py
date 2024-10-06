from django.forms import ModelForm
from django import forms
from .models import User

class UploadForm(ModelForm):
    name = forms.TextInput()
    surname = forms.TextInput()
    email = forms.TextInput()
    class Meta:
        model = User
        fields = ["name","surname","email"]
