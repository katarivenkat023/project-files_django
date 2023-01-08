from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	data="<h1>Index Page</h1>"
	request.session.set_test_cookie()
	return HttpResponse(data)


def checksession(request):
	if request.session.test_cookie_worked():
		print("cookie working properly")
		request.session.delete_test_cookie()
		return HttpResponse("<h1>Checking Page")
		