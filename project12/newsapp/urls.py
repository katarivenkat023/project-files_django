from django.urls import path
from newsapp import views


urlpatterns=[
	path('welcome/',views.home_page),
	path('movies/',views.display_movie_information),
	path('sports/',views.display_sports_information),
	path('politics/',views.display_politics_information),
]