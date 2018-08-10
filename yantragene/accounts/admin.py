from django.contrib import admin
from .models import Profile
# Register your models here.

class AdminProfile(admin.ModelAdmin):
	list_display = ['mobile']

admin.site.register(Profile, AdminProfile)

