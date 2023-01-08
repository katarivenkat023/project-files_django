from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def welcome_client(request):
	msg1='Welcome client'
	date=datetime.datetime.now()
	print(type(date))

	msg2=msg1+'<h1>The Current server time : '+ str(date)+'</h1>'
	return HttpResponse(msg2) 