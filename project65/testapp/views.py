from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
	print('This line is getting printed while processing the request')
	print(10/0)
	s='<h1>Custom middleware application</h1>'
	return HttpResponse(s)