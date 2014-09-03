from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page) # matches function in lists/views.py and resolves to url in lists/urls.py
		
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(expected_html, response.content.decode())