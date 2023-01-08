from django.shortcuts import render

# Create your views here.
from shoppingcartapp.forms import AddItemForm
 
def home_page(request):
	return render(request,'shoppingcartapp/homepage.html')

def additem_view(request):
	form=AddItemForm()
	if request.method=='POST':
		print('expiry date : ',request.session.get_expiry_date())
		print('expiry age : ',request.session.get_expiry_age())
		name=request.POST['name']
		quantity=request.POST['quantity']
		request.session[name]=quantity
	return render(request,'shoppingcartapp/additem.html',{'form':form})

def display_view(request):
	return render(request,'shoppingcartapp/display.html')