from django.contrib import admin
from .models import Department,Events,Coordinator,Participant


class AdminDepartment(admin.ModelAdmin):
	list_display = ['did', 'dname']
	list_editable = ['dname']

class AdminEvents(admin.ModelAdmin):
	list_display = ['eid', 'ename']
	list_editable = ['ename']

class AdminCoordinator(admin.ModelAdmin):
	list_display = ['cname', 'cemail', 'cmobile']
	list_editable = ['cname', 'cemail', 'cmobile']


class AdminParticipant(admin.ModelAdmin):
	list_display = ['team_name', 'events_name', 'member2', 'member3', 'member4', 'member5']

admin.site.register(Department, AdminDepartment)
admin.site.register(Events, AdminEvents)
admin.site.register(Coordinator, AdminCoordinator)
admin.site.register(Participant, AdminParticipant)