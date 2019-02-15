from django.shortcuts import render

from .models import Notifications

def note_view(request):
	return render(request, 'notifications/notifications.html', {'notes':Notifications.objects.all()})