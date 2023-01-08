from django.urls import path
from empapp import views
urlpatterns = [
   path('homepage/',views.homepage),
   path('register/',views.register),
   path('success/',views.success)
]