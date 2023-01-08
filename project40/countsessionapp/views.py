from django.shortcuts import render

# Create your views here.
def count_view(request):
	count=request.session.get('count',0)
	newcount=count+1
	request.session['count']=newcount
	print("expiry age : ",request.session.get_expiry_age())
	print("expiry date : ",request.session.get_expiry_date())
	my_dict={'count':newcount}
	return render(request,'countsessionapp/count.html',context=my_dict)