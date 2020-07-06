from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150, help_text='Email')
    password = forms.CharField()
    class Metas:
        model = User
        fields = ('email','password')

class SignUpForm(forms.Form):
    print("Form is making")
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    username = forms.CharField(max_length=100, help_text='Unique')
    phone_no = forms.IntegerField()
    email = forms.EmailField(max_length=150, help_text='Email')
    gst = forms.IntegerField()
    aadhar = forms.IntegerField()
    pan = forms.IntegerField()
    password1 = forms.CharField()
    password2 =forms.CharField()
    print("Form is made")
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone_no', 'email', 'gst', 'aadhar', 'pan', 'password1',
                  'password2')
