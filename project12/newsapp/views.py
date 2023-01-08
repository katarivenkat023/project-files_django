from django.shortcuts import render


# Create your views here.
def home_page(request):
	return render(request,'newsapp/homepage.html')
def display_movie_information(request):
	main_msg='Latest Movie Information'

	msg1='RRR shooting in progress'
	msg2='Robert and dboss released in this end of the year'
	my_dict={'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request,'newsapp/moviepage.html',context=my_dict)
def display_sports_information(request):
	main_msg='Latest sports Information'

	msg1='IPL held in Dubai'
	msg2='Dhoni got retired'
	my_dict={'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request,'newsapp/sports.html',context=my_dict)
def display_politics_information(request):
	main_msg='Latest Politics Information'

	msg1='Modi will become PM for next election also'
	msg2='Rahul gandhi best batchlor in india'
	my_dict={'main_msg':main_msg,'msg1':msg1,'msg2':msg2}
	return render(request,'newsapp/politics.html',context=my_dict)