from django.shortcuts import render

from .forms import SignUpForm

def home(request):
	sign_form = SignUpForm()
	return render(request, 'home.html', {'sign_form': sign_form})
