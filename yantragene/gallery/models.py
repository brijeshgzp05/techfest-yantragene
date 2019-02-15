from django.db import models

class Images(models.Model):
	imageid = models.CharField(max_length=4)
	imagename = models.ImageField(upload_to='images/gallery', blank=True)

	def __str__(self):
		return self.imageid

