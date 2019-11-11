from django.db import models
import os

class Imageslider(models.Model):
	topic=models.CharField(blank=True,max_length=10)
	description=models.CharField(blank=True,max_length=255)
	imageslider=models.ImageField(upload_to='imageslider/', blank=True, null=True)
	is_active = models.BooleanField(default=False)


