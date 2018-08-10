from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^notifications/', include('notifications.urls', namespace='notifications')),
    url(r'^aboutus/', include('aboutus.urls', namespace='aboutus')),
    url(r'^contactus/', include('contactus.urls', namespace='contactus')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

