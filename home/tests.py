from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .forms import SignUpForm

from .views import home

class HomeTests(TestCase):
	def setUp(self):
		url = reverse('home')
		self.response = self.client.get(url)

	def test_home_view_status_code(self):
		self.assertEquals(self.response.status_code, 200)
	
	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)

	def test_csrf(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')
	
	def test_contains_form(self):
		form = self.response.context.get('form')
		self.assertIsInstance(form, SignUpForm)

