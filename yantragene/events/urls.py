from django.conf.urls import url
from . import views


# app_name = "events"

urlpatterns = [

	url(r'^$', views.events_view, name='events'),
	url(r'^detail/(?P<id>\d+)/', views.event_detail, name="detail"),
	url(r'^register/$', views.register_view, name="register"),
	
	
]