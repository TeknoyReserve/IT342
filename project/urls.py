from django.urls import path
from . import views

app_name = 'project'

# path('<int:a>/<int:b>' , views.Home.as_view(), name="home_view") URL DISPATCHER
urlpatterns= [
	path('' , views.Home.as_view(), name="home_view"),
	
]