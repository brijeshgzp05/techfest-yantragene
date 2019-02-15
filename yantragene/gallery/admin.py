from django.contrib import admin

from .models import Images

class AdminImages(admin.ModelAdmin):
	list_display = ['imageid', 'imagename']

admin.site.register(Images, AdminImages)
