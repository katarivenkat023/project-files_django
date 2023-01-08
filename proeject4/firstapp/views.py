from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app(request):
	data='<h1>Thanks for connecting to First application</h1>'
	return HttpResponse(data)