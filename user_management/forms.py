from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'  # You can specify the fields you want to display in the form
