from django.conf.urls import url 
from . import views

# app_name = 'home'

urlpatterns = [
	url(r'^$', views.home_view, name="home")
]