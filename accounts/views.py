from pickle import FALSE, TRUE
from django.contrib.auth import login as auth_login, authenticate
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm

from home.forms import SignUpForm

def signup(request):
	if request.method == 'POST' and request.is_ajax():
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return JsonResponse({"success": True, "message": "User create successfully"})
		else:
			form_template = render_to_string('includes/form.html', {"form": form})
			return JsonResponse({"success": False, "form": form_template})

def login(request):
	if request.method == 'POST' and request.is_ajax():
		form = AuthenticationForm(None, request.POST)
		if form.is_valid():
			user = form.get_user()
			auth_login(request, user)
			return JsonResponse({"success": True})
		else:
			form_template = render_to_string('includes/form.html', {"form": form})
			return JsonResponse({"success": False, "form": form_template})
