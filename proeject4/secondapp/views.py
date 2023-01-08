from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def second_app(request):
	data='<h1>Thanks for connecting to second application</h1>'
	return HttpResponse(data)