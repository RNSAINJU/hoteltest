from django.db import models


class Package(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=12, decimal_places=2)
	discounted_price = models.DecimalField(max_digits=12, decimal_places=2)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='packages/%y/%m/', blank=True, null=True)

	is_active = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Hotel(models.Model):
	name = models.CharField(max_length=255)
	link = models.URLField(blank=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='packages/%y/%m/', blank=True, null=True)

	is_active = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Review(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	contact = models.CharField(max_length=15, blank=True)
	review = models.TextField()
	stars = models.DecimalField(max_digits=2, decimal_places=1)
	image = models.ImageField(upload_to='review/', blank=True, null=True)

	date_created = models.DateTimeField(auto_now_add=True)
	is_featured = models.BooleanField(default=True)

	def __str__(self):
		return self.name
