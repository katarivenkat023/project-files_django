from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def corona_vijayanagar(request):
	data='<h1>Corona cases in viajayanagar : 500 </h1>'
	return HttpResponse(data)
def corona_btm(request):
	data='<h1>Corona cases in btm : 400 </h1>'
	return HttpResponse(data)
def corona_hebbal(request):
	data='<h1>Corona cases in hebbal : 300 </h1>'