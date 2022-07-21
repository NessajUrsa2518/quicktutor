from pickle import FALSE, TRUE
from django.contrib.auth import login as auth_login, authenticate
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator

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

def reset(request):
	if request.method == 'POST' and request.is_ajax():
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			users = form.get_users(form.cleaned_data['email'])
			if users:
				opts = {
					'use_https': request.is_secure(),
					'token_generator': default_token_generator,
					'from_email': None,
					'email_template_name': 'password_reset_email.html',
					'subject_template_name': 'password_reset_subject.txt',
					'request': request,
					'html_email_template_name': None,
					'extra_email_context': None,
				}
				form.save(**opts)
			return JsonResponse({"success": True})
		else:
			form_template = render_to_string('includes/form.html', {"form": form})
			return JsonResponse({"success": False, "form": form_template})
