from django.contrib import admin

from .models import Package, Hotel, Review, Enquiry


admin.site.register(Package)
admin.site.register(Hotel)
admin.site.register(Review)
admin.site.register(Enquiry)
