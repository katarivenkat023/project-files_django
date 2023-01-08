from django.urls import path
from studentapp import views

urlpatterns = [
				path('homepage/', views.home_page),
				path('register/', views.register_data),
				path('thankyou/', views.thank_you),
    
   
]
