from django.contrib import admin
from .models import Notifications
# Register your models here.

class AdminNotifications(admin.ModelAdmin):
	list_display = ['nid', 'ndetail']
	list_editable = ['ndetail']
	
admin.site.register(Notifications, AdminNotifications)
