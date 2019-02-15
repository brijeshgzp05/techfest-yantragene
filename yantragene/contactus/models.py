from django.db import models

# Create your models here.

class Feedback(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	review = models.CharField(max_length=250)

	def __str__(self):
		return self.name
