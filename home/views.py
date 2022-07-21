from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

from .forms import SignUpForm

def home(request):
	sign_form = SignUpForm()
	login_form = AuthenticationForm()
	reset_form = PasswordResetForm()
	return render(request, 'home.html', {'sign_form': sign_form, 'login_form': login_form, 'reset_form': reset_form})
