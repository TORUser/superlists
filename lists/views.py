#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><h1><title>To-Do lists</title></h1></html>')