from django.db import models

# Create your models here.

class Notifications(models.Model):
	nid = models.IntegerField()
	ndetail = models.CharField(max_length=200)

	def __str__(self):
		return self.ndetail
