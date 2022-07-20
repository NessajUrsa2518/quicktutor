from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class LogInForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"placeholder": "Username",
				"class": "form-control"
			}
		))
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"placeholder": "Password",
				"class": "form-control"
			}
		))
