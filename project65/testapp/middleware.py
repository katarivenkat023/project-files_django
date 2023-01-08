

from django.http import HttpResponse

class AppUnderMaintainance(object):
	def __init__(self,get_response):
		#get_response is the objectreference of the middleware response
		self.get_response = get_response

	def __call__(self,request):
		s='<h1>Server is under Maintainance</h1>'
		return HttpResponse(s)

