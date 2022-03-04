from django.urls import path
from . import views

app_name = 'project'

urlpatterns= [
	path('home', views.Home.as_view(), name="home_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('user-dashboard', views.UsersDashboard.as_view(), name="user-dashboard_view"),
	path('room-dashboard', views.RoomDashboard.as_view(), name="room-dashboard_view"),
	path('dummy', views.Dummy.as_view(), name="dummy"),

	
]