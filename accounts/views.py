from pickle import FALSE, TRUE
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string

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
