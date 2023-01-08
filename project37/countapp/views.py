from django.shortcuts import render

# Create your views here.
def count_view(request):
	if 'count' in request.COOKIES:
		newcount=int(request.COOKIES['count'])+1
	else:
		newcount=1
	my_dict={'count':newcount}
	response=render(request,'countapp/count.html',context=my_dict)
	response.set_cookie('count',newcount)
	return response