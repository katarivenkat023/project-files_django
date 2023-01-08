from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def corona_ramakrishnanagar(request):
	data='<h1>Corona cases in ramakirihananagar : 400 </h1>'
	return HttpResponse(data)
def corona_kdroad(request):
	data='<h1>Corona cases in kdroad : 500 </h1>'
	return HttpResponse(data)
def corona_vijayanagar(request):
	data='<h1>Corona cases in viajayanagar : 300 </h1>'
	return HttpResponse(data)