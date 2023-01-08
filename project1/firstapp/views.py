from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display_data(request):
	data='<marquee style="color:red" direction="right">Welcome to learn django and rest API by SANDESH</marquee>'
	return HttpResponse(data)