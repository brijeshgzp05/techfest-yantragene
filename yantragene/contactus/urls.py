from django.conf.urls import url

from . import views

# app_name = "contactus"

urlpatterns = [
	url(r'^$', views.contactus_view, name="contactus"),
	url(r'^feedback/$', views.feedback_view, name="feedback"),
]