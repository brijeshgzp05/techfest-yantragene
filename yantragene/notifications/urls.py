from django.conf.urls import url 
from .import views

# app_name = 'notifications'

urlpatterns = [
	url(r'^$', views.note_view, name="notifications")
]