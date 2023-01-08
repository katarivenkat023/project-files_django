from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def middleware_check(request):
	name=request.user
	print(name)
	response='''
			<html>
			<body>
			<h1>This is the response send from server with default middleware</h1>
			</body>
			</html>
			'''
	return HttpResponse(response)