from django.urls import path
from . import views

app_name = 'project'

urlpatterns= [
	path('', views.Home.as_view(), name="home_view"),
	
]