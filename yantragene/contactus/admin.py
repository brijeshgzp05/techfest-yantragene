from django.contrib import admin
from .models import Feedback

# Register your models here.
class AdminFeedback(admin.ModelAdmin):
	list_display = ['name', 'email', 'review']

admin.site.register(Feedback,AdminFeedback)