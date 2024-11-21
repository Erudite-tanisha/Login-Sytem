from django import forms
from .models import UserDetails


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length= 20, widget= forms.TextInput(attrs={'class': 'form-control'}), label= 'First Name')
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Last Name')
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username')
    email = forms.EmailField(label= 'Email', required=False,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')

class LoginForm(forms.Form):
      username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}),max_length=50)
      password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Meta:
        model = UserDetails 
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


 