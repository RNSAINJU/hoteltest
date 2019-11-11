from django.db import models

# import os
# import random
# def get_filename_ext(filepath):
# 	base_name=os.path.basename(filepath)
# 	name,ext=os.path.splitext(base_name)
# 	return name,ext

# def upload_image_path(instance, filename):
# 	new_filename=random.randint(1,3910209312)
# 	name,ext=get_filename_ext(filename)
# 	final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
# 	return "post-image/{final_filename}".format(
# 		new_filename=new_filename,
# 		final_filename=final_filename
# 		)


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
	is_recommended=models.BooleanField(default=False)
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

class Enquiry(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	mobilenumber=models.CharField(max_length=14)
	message=models.TextField()

	def __str__(self):
		return self.name

