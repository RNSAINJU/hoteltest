from django.db import models
import os

class Imageslider(models.Model):
	topic=models.CharField(blank=True,max_length=10)
	description=models.CharField(blank=True,max_length=255)
	imageslider=models.ImageField(upload_to='imageslider/', blank=True, null=True)
	is_active = models.BooleanField(default=False)

class AboutContent(models.Model):
	image = models.ImageField(upload_to='about/')
	title = models.CharField(max_length=255)
	description  = models.TextField()
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.title
		
class Backgroundimage(models.Model):
	name = models.CharField(blank=True, max_length=10)
	image = models.ImageField(upload_to='backgroundimage/', blank=True, null=True)
