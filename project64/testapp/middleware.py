class ExecutionFlowMiddleware(object):
	def __init__(self,get_response):
		#get_response is the objectreference of the middleware response
		self.get_response = get_response

	def __call__(self,request):
		print('This line represents the pre processing of request')
		response = self.get_response(request)
		print('This line represents the post processing of response')
		return response