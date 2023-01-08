 from django.shortcuts import render
from cartapp.forms import ItemForm

# Create your views here.
def home_page(request):
	return render(request,'cartapp/homepage.html')

def add_item(request):
	form=ItemForm()
	my_dict={'form':form}
	response=render(request,'cartapp/additem.html',context=my_dict)
	if request.method=="POST":
		form=ItemForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			quantity=form.cleaned_data['quantity']
			response.set_cookie(name,quantity,180)

	return response

def display_view(request):
	return render(request,'cartapp/display.html')