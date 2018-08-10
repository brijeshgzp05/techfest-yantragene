from django.db import models
from accounts.models import Profile
class Department(models.Model):
	
	did = models.IntegerField()
	dname = models.CharField(max_length=50)
	dimage = models.ImageField(upload_to='images/departments', blank=True)

	def __str__(self):
		return self.dname


class Events(models.Model):
	
	eid = models.IntegerField()
	ename = models.CharField(max_length=30)
	department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)


	def __str__(self):
		return self.ename

class Coordinator(models.Model):
	
	cname = models.CharField(max_length=20)
	cmobile = models.CharField(max_length=13)
	cemail = models.EmailField()
	cimage = models.ImageField(upload_to='images/coordinators', blank=True)
	events = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.cname


class Participant(models.Model):

	events = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	team_name = models.CharField(max_length=30, blank=True, null=True)
	events_name = models.CharField(max_length=30, blank=True, null=True)
	member2 = models.CharField(max_length=50, blank=True, null=True)
	member3 = models.CharField(max_length=50, blank=True, null=True)
	member4 = models.CharField(max_length=50, blank=True, null=True)
	member5 = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.team_name

