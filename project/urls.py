from django.urls import path
from . import views

app_name = 'project'

urlpatterns= [
	path('home', views.Home.as_view(), name="home_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('user-dashboard', views.UsersDashboard.as_view(), name="user-dashboard_view"),
	path('room-dashboard', views.RoomDashboard.as_view(), name="room-dashboard_view"),
	path('room-reservation', views.RoomReservation.as_view(), name="room-reservation_view"),
	path('about', views.About.as_view(), name="about_view"),
	path('services', views.Services.as_view(), name="services_view"),
	path('gallery', views.Gallery.as_view(), name="gallery_view"),
	path('team', views.Team.as_view(), name="team_view"),
	path('contact', views.Contact.as_view(), name="contact_view"),
	path('login', views.Login.as_view(), name="login_view"),

	
]