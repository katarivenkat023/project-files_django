from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def corona_sathyamangala(request):
	data='<h1>Corona cases in sathyamanagala : 500 </h1>'
	return HttpResponse(data)
def corona_chennarayapatna(request):
	data='<h1>Corona cases in chennarayapatna : 400 </h1>'
	return HttpResponse(data)
def corona_arsikere(request):
	data='<h1>Corona cases in arsikere : 900 </h1>'
	return HttpResponse(data)