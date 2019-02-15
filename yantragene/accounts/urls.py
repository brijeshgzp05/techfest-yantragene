from django.conf.urls import url
from . import views

# app_name = "accounts"

urlpatterns = [
	url(r'^register/$', views.register_view, name="register"),
	url(r'^login/$', views.login_view, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^profile/(?P<id>\d+)/$', views.profile_view, name="profile"),
	url(r'^delete/(?P<id>\d+)/(?P<proid>\d+)/$', views.delete_event, name="delete"),
]