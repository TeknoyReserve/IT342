from django.urls import path
from . import views

app_name = 'project'

urlpatterns= [
	path('home', views.Home.as_view(), name="home_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('room-dashboard', views.RoomDashboard.as_view(), name="room-dashboard_view"),
	
]