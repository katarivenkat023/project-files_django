
from django.urls import path
from bangalorecoronaapp import views as bangalore


urlpatterns = [
    path('vijayanagar/',bangalore.corona_vijayanagar),
    path('btm/',bangalore.corona_btm),
    path('hebbal/',bangalore.corona_hebbal),
]
