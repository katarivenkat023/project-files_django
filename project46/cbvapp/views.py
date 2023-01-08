from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
class welcome(View):
	def get(self,request):
		data="<h1>Welcome to Study Online...this is from View class"
		return HttpResponse(data)
